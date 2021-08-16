# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QFont, QFontDatabase
from syntax_highlighter import PythonSyntaxHighlighter
import subprocess
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QPushButton
from PySide6.QtCore import QDir, QFile, QTranslator, Slot

from ui_pythoneditor import Ui_PythonEditor

class PythonEditor(QWidget):
    def __init__(self):
        super(PythonEditor, self).__init__()
        self.ui = Ui_PythonEditor()
        self.ui.setupUi(self)

        # Setup variables
        self.python_path = "C:\\Python39\\python.exe"
        self.filename = None

        # Setup buttons
        self.ui.newButton.clicked.connect(self.new_document)
        self.ui.openButton.clicked.connect(self.open)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.saveAsButton.clicked.connect(self.save_as)
        self.ui.runButton.clicked.connect(self.run)
        
        # Setup editor
        print(QFontDatabase.families())
        font = QFont("Fira Code", 24, QFont.Bold)
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
    def open(self):
        # Use QFileDialog to get target filename.
        self.filename, _ = QFileDialog.getOpenFileName(self, 
            caption="Open file",
            dir="./",
            filter="Python Script (*.py)")
        print(f"Opened file: {self.filename}")

        # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self.filename}")

        # Open file and display on editor.
        with open(self.filename, "r", encoding="UTF-8") as file:
            self.ui.editorEdit.setText(file.read())
    
    @Slot()
    def save(self):
        # Open file
        with open(self.filename, "w", encoding="UTF-8") as file:
            file.write(self.ui.editorEdit.toPlainText())
    
    @Slot()
    def save_as(self):
        # Use QFileDialog to select new filename
        self.filename, _ = QFileDialog.getSaveFileName(self,
            caption="Save file",
            dir="./",
            filter="Python Script (*.py)")
        
        # Display name on label.
        self.ui.filenameLabel.setText(f"File: {self.filename}")
        
        # Save file
        self.save()

    @Slot()
    def run(self):
        # Save
        self.save()

        # Execute
        proc = subprocess.Popen([self.python_path, self.filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        # NOTE: The UI will freeze while executing. Consider using another thread.

        # Update output QTextBrowser.
        # NOTE: The encoding of the stdout is to be made clear, right now it seems to be Big5.
        out = str(out, encoding="Big5")
        err = str(err, encoding="Big5") if err is not None else ''
        self.ui.outputTextBrowser.setText(out + err)


if __name__ == "__main__":
    app = QApplication([])
    widget = PythonEditor()
    widget.show()
    sys.exit(app.exec())
