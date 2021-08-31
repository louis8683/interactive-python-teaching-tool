from PySide6.QtWidgets import QApplication, QWidget
from layouts.ui_pythoneditor import Ui_PythonEditor

import sys

class PythonEditor(QWidget):
    def __init__(self):
        super(PythonEditor, self).__init__()
        self.ui = Ui_PythonEditor()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    widget = PythonEditor()
    widget.show()
    sys.exit(app.exec())
