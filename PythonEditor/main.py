# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QFont, QFontDatabase, QPalette, QTextCursor, Qt
from syntax_highlighter import PythonSyntaxHighlighter
import subprocess
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QTableWidgetItem, QWidget, QPushButton
from PySide6.QtCore import QDir, QFile, QTranslator, Slot

from script.analyze_src_code import SourceCodeAnalyzer

from ui_pythoneditor import Ui_PythonEditor

class PythonEditor(QWidget):
    def __init__(self):
        super(PythonEditor, self).__init__()
        self.ui = Ui_PythonEditor()
        self.ui.setupUi(self)

        # Setup variables
        self.python_path = "C:\\Python39\\python.exe"
        self.filename = ""
        self.highlighted_lines, self.last_highlighted_lines = [], []

        # Setup buttons
        self.ui.newButton.clicked.connect(self.new_document)
        self.ui.openButton.clicked.connect(self.open)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.saveAsButton.clicked.connect(self.save_as)
        self.ui.runButton.clicked.connect(self.run)
        self.ui.lineByLineButton.clicked.connect(self.run_line_by_line)
        
        # Setup editor
        font = QFont("Fira Code", 12, QFont.Bold)
        self.ui.editorEdit.setFont(font)
        self.highlighter = PythonSyntaxHighlighter(self.ui.editorEdit.document())

    @Slot()
    def new_document(self):
        # Use QFileDialog to select new filename
        self.filename, _ = QFileDialog.getSaveFileName(self,
            caption="New file",
            dir="./",
            filter="Python Script (*.py)")
        
       # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self.filename}")

    @Slot()
    def open(self) -> bool:
        # Use QFileDialog to get target filename.
        self.filename, _ = QFileDialog.getOpenFileName(self, 
            caption="Open file",
            dir="./",
            filter="Python Script (*.py)")
        print(f"Opened file: {self.filename}")

        # No file selected
        if self.filename == "":
            return False

        # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self.filename}")

        # Open file and display on editor.
        with open(self.filename, "r", encoding="UTF-8") as file:
            self.ui.editorEdit.setText(file.read())
        
        return True

    @Slot()
    def save(self) -> bool:
        # Use save_as if file doesn't exist
        if self.filename == "":
            return self.save_as()
        else:
            # Open file
            with open(self.filename, "w", encoding="UTF-8") as file:
                file.write(self.ui.editorEdit.toPlainText())
            return True

    @Slot()
    def save_as(self) -> bool:
        # Use QFileDialog to select new filename
        self.filename, _ = QFileDialog.getSaveFileName(self,
            caption="Save file",
            dir="./",
            filter="Python Script (*.py)")
        
        # No file selected
        if self.filename == "":
            return False

        # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self.filename}")
        
        # Save file
        self.save()
        
        return True

    @Slot()
    def run(self) -> bool:
        # Save, return False is failed
        if self.save() is False:
            return False

        # Execute
        proc = subprocess.Popen([self.python_path, self.filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        # NOTE: The UI will freeze while executing. Consider using another thread.

        # Update output QTextBrowser.
        # NOTE: The encoding of the stdout is to be made clear, right now it seems to be Big5.
        out = str(out, encoding="Big5")
        err = str(err, encoding="Big5") if err is not None else ''
        self.ui.outputTextBrowser.setText(out + err)
    
    @Slot()
    def run_line_by_line(self) -> bool:
        # Save, return False is failed
        if self.save() is False:
            return False
        
        # Load analyzer if not loaded
        try:
            self.analyzer
        except AttributeError:
            self.analyzer = SourceCodeAnalyzer(self.filename)
            self.action_no = 0
            self.highlighted_lines = [self.analyzer.actions[self.action_no][0]]
            print(self.analyzer.actions)

        # Last action?
        if self.action_no == len(self.analyzer.actions):
            # Remove highlights
            self.last_highlighted_lines = self.highlighted_lines
            self.highlighted_lines = []
            self.highlight_lines(self.highlighted_lines, self.last_highlighted_lines, line_no_start=self.analyzer.offset)
            # Reset tables
            self.ui.globalVarTableWidget.setRowCount(0)
            self.ui.globalVarTableWidget.setColumnCount(0)
            self.ui.localVarTableWidget.setRowCount(0)
            self.ui.localVarTableWidget.setColumnCount(0)
            # Delete analyzer
            del self.analyzer
            print("Last line") # TODO: hint that we had reached the last line
            return False
            
        # Highlight
        self.last_highlighted_lines = self.highlighted_lines
        self.highlighted_lines = [self.analyzer.actions[self.action_no][0]]
        self.highlight_lines(self.highlighted_lines, self.last_highlighted_lines, line_no_start=self.analyzer.offset)
        
        # Update output for print()
        if "print" in self.analyzer.actions[self.action_no][1]:
            print_text = self.analyzer.actions[self.action_no][1]["print"]
            cursor = QTextCursor(self.ui.outputTextBrowser.document())
            cursor.movePosition(QTextCursor.End)
            cursor.insertText(print_text)

        # Update variables
        record_no = self.analyzer.actions[self.action_no][2]
        vars = self.analyzer.get_variables(record_no)
        self.ui.globalVarTableWidget.setRowCount(len(vars["global"]))
        self.ui.globalVarTableWidget.setColumnCount(2)
        for i, var_name in enumerate(vars["global"]):
            self.ui.globalVarTableWidget.setItem(i, 0, QTableWidgetItem(var_name))
            self.ui.globalVarTableWidget.setItem(i, 1, QTableWidgetItem(str(vars["global"][var_name])))
        self.ui.localVarTableWidget.setRowCount(len(vars["local"]))
        self.ui.localVarTableWidget.setColumnCount(2)
        for i, var_name in enumerate(vars["local"]):
            self.ui.localVarTableWidget.setItem(i, 0, QTableWidgetItem(var_name))
            self.ui.localVarTableWidget.setItem(i, 1, QTableWidgetItem(str(vars["local"][var_name])))
        
        # Increment action no
        self.action_no += 1
        
        return True

    def highlight_lines(self, highlight: list[int], old_highlight: list[int], color=Qt.yellow, line_no_start=0):
        for line in set(highlight + old_highlight): # Only go through lines highlighted or previously highlighted
            block = self.ui.editorEdit.document().findBlockByLineNumber(line - line_no_start)
            cursor = QTextCursor(block)
            cursor.select(cursor.LineUnderCursor)
            if line in highlight:
                format = block.charFormat()
                format.setBackground(Qt.yellow)
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
