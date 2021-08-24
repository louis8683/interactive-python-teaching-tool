# This Python file uses the following encoding: utf-8
from types import BuiltinFunctionType, BuiltinMethodType, FunctionType, ModuleType
from typing import Any
from PySide6.QtGui import QFont, QFontDatabase, QPalette, QTextCharFormat, QTextCursor, Qt
from syntax_highlighter import PythonSyntaxHighlighter
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QInputDialog, QMainWindow, QSlider, QTableWidget, QTableWidgetItem, QWidget, QPushButton
from PySide6.QtCore import QDir, QFile, QTranslator, Slot

from script.analyze_src_code import SourceCodeAnalyzer
from script.custom_types import ModuleTypeCopy, CustomClassCopy

from ui_pythoneditor import Ui_PythonEditor
from settings import Settings

class PythonEditor(QWidget):
    def __init__(self):
        super(PythonEditor, self).__init__()
        self.ui = Ui_PythonEditor()
        self.ui.setupUi(self)

        # Setup variables

        # Public
        
        # Private
        self._settings = Settings()

        self._filename = self._settings.path["last_opened_file"]

        self._current_line, self._last_line = -1, -1 # These numbers are not important
        self._analyzer = None

        # UI text setup
        # for var_name in dir(self.ui):
        #     # Find the QWidgets
        #     var = eval(f"self.ui.{var_name}")
        #     if issubclass(type(var), QWidget):
        #         var.setFont(self._settings.font["ui"])
            

        # Editor text format setup
        self._default_text_edit_format = QTextCharFormat()
        self._default_text_edit_format.setBackground(self.ui.editorEdit.palette().color(QPalette.Base))
        self._default_text_edit_format.setFont(self._settings.font["editor"])
        self._last_plain_text = ""

        # Setup buttons
        self.ui.newButton.clicked.connect(self.new_document)
        self.ui.openButton.clicked.connect(self.open)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.saveAsButton.clicked.connect(self.save_as)
        self.ui.runButton.clicked.connect(self.run)
        self.ui.lineByLineButton.clicked.connect(self.run_line_by_line)
        
        # Setup editor
        self.ui.editorEdit.setFont(self._default_text_edit_format.font())
        self.ui.editorEdit.textCursor().setBlockCharFormat(self._default_text_edit_format)
        self._highlighter = PythonSyntaxHighlighter(self.ui.editorEdit.document())
        self.ui.editorEdit.textChanged.connect(self.on_text_changed)

        if self._filename != "":
            self.open(self._filename)

        # Setup browser

        # Setup slider
        # self.ui.stepSlider.sliderMoved.connect(self.on_slider_moved)


    @Slot()
    def new_document(self):
        # Use QFileDialog to select new filename
        self._filename, _ = QFileDialog.getSaveFileName(self,
            caption="New file",
            dir="./",
            filter="Python Script (*.py)")
        
       # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self._filename}")

    @Slot()
    def open(self, filename="") -> bool:
        if not filename: # filename is False if UI button is clicked.
            # Use QFileDialog to get target filename.
            filename, _ = QFileDialog.getOpenFileName(self, 
                caption="Open file",
                dir="./",
                filter="Python Script (*.py)")
            print(f"Opening file: {filename}")

            # No file selected
            if filename == "":
                return False

        try:
            # Open file and display on editor.
            with open(filename, "r", encoding="UTF-8") as file:
                self.ui.editorEdit.setText(file.read())

            # Display name on label.
            self.ui.filenameLabel.setText(f"File: {filename}")
        except FileNotFoundError:
            return False
        
        # Update filename
        self._filename = filename

        # Update the last_opened_file
        self._settings.path["last_opened_file"] = self._filename
        self._settings.save()

        return True

    @Slot()
    def save(self) -> bool:
        # Use save_as if file doesn't exist
        if self._filename == "":
            return self.save_as()
        else:
            # Open file
            with open(self._filename, "w", encoding="UTF-8") as file:
                file.write(self.ui.editorEdit.toPlainText())
            return True

    @Slot()
    def save_as(self) -> bool:
        # Use QFileDialog to select new filename
        self._filename, _ = QFileDialog.getSaveFileName(self,
            caption="Save file",
            dir="./",
            filter="Python Script (*.py)")
        
        # No file selected
        if self._filename == "":
            return False

        # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self._filename}")
        
        # Save file
        self.save()
        
        return True

    @Slot()
    def run(self) -> bool:
        # Save, return False is failed
        if self.save() is False:
            return False

        # # Execute, NOTE: The UI will freeze while executing.
        # proc = subprocess.Popen([self._settings.path["python_path"], self._filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # out, err = proc.communicate()

        # Update output QTextBrowser.
        # # NOTE: The encoding of the stdout is to be made clear, right now it seems to be Big5.
        # out = str(out, encoding="Big5")
        # err = str(err, encoding="Big5") if err is not None else ''
        # self.ui.outputTextBrowser.setText(out + err)

        while self.run_line_by_line():
            pass
    
    @Slot()
    def run_line_by_line(self) -> bool:
        # Save, return False is failed
        if self.save() is False:
            return False
        
        # Load analyzer if not loaded
        if self._analyzer is None:
            # init variables
            self._analyzer = SourceCodeAnalyzer(self._filename, python_path=self._settings.path["python_path"])
            self._action_no = 0
            self._input_list = []
            # clear output
            self.ui.outputTextBrowser.clear()
            # setup slider
            self.ui.stepSlider.setMaximum(len(self._analyzer.actions))
            print(self._analyzer.actions)

        # Last action?
        if self._action_no == len(self._analyzer.actions):
            self._line_by_line_clean_up()
            print("Last line") # TODO: hint that we had reached the last line
            return False

        # Extract action
        line_no, events, record_no = self._analyzer.actions[self._action_no]
        
        # Move slider
        self.ui.stepSlider.setValue(self._action_no)

        # ORDER: input -> error -> general

        # Input
        if "input" in events:
            # Move highlight
            self._move_current_line_highlight(line_no)

            # Get input from user
            text, stat = QInputDialog(self).getText(self, "input()", self._analyzer.actions[self._action_no][1]["input"])
            if stat:
                # Put input into input list
                self._input_list.append(text)
                # Rerun analyzer
                self._analyzer.rerun(self._input_list)
                # Re-extract actions
                line_no, events, record_no = self._analyzer.actions[self._action_no]
                print(self._analyzer.actions)
            else:
                # User didn't input
                return False
        
        # Error
        if "error" in events:
            # Move highlight
            self._move_current_line_highlight(line_no)

            # Show error message on output
            error = events["error"]
            error_msg = f"{str(type(error))[8:-2]}: {str(error)}"
            # Write to output window.
            format = QTextCharFormat()
            format.setForeground(Qt.red)
            self._write_to_output(error_msg, format)

            self._action_no += 1 # trigger last line
            return False


        # General statements
        # Move highlight
        self._move_current_line_highlight(line_no)

        # Update output for print()
        if "print" in events:
            self._write_to_output(events["print"])

        # Update variables
        vars = self._analyzer.get_variables(record_no)
        self.ui.globalVarTableWidget.setRowCount(len(vars["global"]))
        self.ui.globalVarTableWidget.setColumnCount(3)
        for i, var_name in enumerate(vars["global"]):
            self._set_table_row(self.ui.globalVarTableWidget, i, var_name, vars["global"][var_name])
            if ("g_added" in events and var_name in events["g_added"]) \
                    or ("g_changed" in events and var_name in events["g_changed"]):
                self._hightlight_row(self.ui.globalVarTableWidget, i)
        self.ui.localVarTableWidget.setRowCount(len(vars["local"]))
        self.ui.localVarTableWidget.setColumnCount(3)
        for i, var_name in enumerate(vars["local"]):
            self._set_table_row(self.ui.localVarTableWidget, i, var_name, vars["local"][var_name])
            if ("l_added" in events and var_name in events["l_added"]) \
                    or ("l_changed" in events and var_name in events["l_changed"]):
                self._hightlight_row(self.ui.localVarTableWidget, i)
        
        # Increment action no
        self._action_no += 1
        
        return True


    @Slot()
    def on_text_changed(self):
        # Did plain text changed?
        if self._last_plain_text != self.ui.editorEdit.toPlainText():
            # NOTE: should we use key event detection for more complex controls?
            self._tab_replacement = "    "
            # Replace tabs in the block with 4 spaces
            cursor = self.ui.editorEdit.textCursor()
            position = cursor.position()
            cursor.select(cursor.LineUnderCursor)
            # Only replace line when there is tab. (to avoid recurrent on_text_changed() calls.)
            if "\t" in cursor.selectedText():
                new_text = cursor.selectedText().replace("\t", self._tab_replacement)
                cursor.removeSelectedText()
                cursor.insertText(new_text)
                cursor.setPosition(position + len(self._tab_replacement) - 1)
                self.ui.editorEdit.setTextCursor(cursor)

            # Update plain text.
            self._last_plain_text = self.ui.editorEdit.toPlainText()    
            # is line-by-line running?
            if self._analyzer is not None:
                # end the line-by-line mode
                self._action_no = len(self._analyzer.actions)
                self.run_line_by_line()
                # Set the cursor format to the default input format (remove highlights etc.)
                self.ui.editorEdit.textCursor().setBlockCharFormat(self._default_text_edit_format)
    
    # @Slot()
    # def on_slider_moved(self):
    #     # line-by-line running?
    #     if self._analyzer is not None:
    #         # TODO
    #         pass

    def _move_current_line_highlight(self, current_line_no:int, color=Qt.yellow):
        self._highlight_lines([current_line_no], [self._last_line], color=color, line_no_start=self._analyzer.offset)
        self._last_line = current_line_no

    def _write_to_output(self, msg:str, format:QTextCharFormat=None):
        cursor = QTextCursor(self.ui.outputTextBrowser.document())
        cursor.movePosition(QTextCursor.End)
        if format:
            cursor.insertText(msg, format)
        else:
            cursor.insertText(msg)

    def _set_table_row(self, table:QTableWidget, row, var_name:str, var_value:Any):
        table.setItem(row, 0, QTableWidgetItem(var_name))
        if type(var_value) in (ModuleTypeCopy, ModuleType):
            table.setItem(row, 1, QTableWidgetItem("-"))
            table.setItem(row, 2, QTableWidgetItem("module"))
        elif type(var_value) == CustomClassCopy:
            table.setItem(row, 1, QTableWidgetItem("-"))
            table.setItem(row, 2, QTableWidgetItem(var_value.type_string[8:-2]))
        elif type(var_value) in (FunctionType, BuiltinFunctionType):
            table.setItem(row, 1, QTableWidgetItem("-"))
            table.setItem(row, 2, QTableWidgetItem(str(type(var_value))[8:-2]))
        else:   
            table.setItem(row, 1, QTableWidgetItem(str(var_value)))
            table.setItem(row, 2, QTableWidgetItem(str(type(var_value))[8:-2]))
    
    def _reset_tables(self):
        self.ui.globalVarTableWidget.setRowCount(0)
        self.ui.globalVarTableWidget.setColumnCount(0)
        self.ui.localVarTableWidget.setRowCount(0)
        self.ui.localVarTableWidget.setColumnCount(0)
    
    def _line_by_line_clean_up(self):
        self._remove_highlights()
        self._reset_tables()
        self._analyzer = None

    def _hightlight_row(self, table:QTableWidget, row, color=Qt.yellow):
        for col in range(table.columnCount()):
            table.item(row, col).setBackground(color)

    def _remove_highlights(self):
        self._highlight_lines([], list(range(self.ui.editorEdit.document().lineCount())))

    def _highlight_lines(self, highlight: list[int], old_highlight: list[int], color=Qt.yellow, line_no_start=0):
        for line in set(highlight + old_highlight): # Only go through lines highlighted or previously highlighted
            if type(line) is int and 0 <= line - line_no_start < self.ui.editorEdit.document().lineCount():
                block = self.ui.editorEdit.document().findBlockByLineNumber(line - line_no_start)
                cursor = QTextCursor(block)
                cursor.select(cursor.LineUnderCursor)
                if line in highlight:
                    format = block.charFormat()
                    format.setBackground(color)
                else:
                    format = block.charFormat()
                    palette = self.ui.editorEdit.palette()
                    format.setBackground(palette.color(QPalette.Base))
                cursor.setCharFormat(format)

if __name__ == "__main__":
    app = QApplication([])
    widget = PythonEditor()
    widget.show()
    sys.exit(app.exec())
