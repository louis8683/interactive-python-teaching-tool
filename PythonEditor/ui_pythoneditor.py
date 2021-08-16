# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_PythonEditor(object):
    def setupUi(self, PythonEditor):
        if not PythonEditor.objectName():
            PythonEditor.setObjectName(u"PythonEditor")
        PythonEditor.resize(471, 414)
        self.verticalLayout = QVBoxLayout(PythonEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newButton = QPushButton(PythonEditor)
        self.newButton.setObjectName(u"newButton")

        self.horizontalLayout.addWidget(self.newButton)

        self.openButton = QPushButton(PythonEditor)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(PythonEditor)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.saveAsButton = QPushButton(PythonEditor)
        self.saveAsButton.setObjectName(u"saveAsButton")

        self.horizontalLayout.addWidget(self.saveAsButton)

        self.runButton = QPushButton(PythonEditor)
        self.runButton.setObjectName(u"runButton")

        self.horizontalLayout.addWidget(self.runButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.filenameLabel = QLabel(PythonEditor)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.verticalLayout.addWidget(self.filenameLabel)

        self.editorEdit = QTextEdit(PythonEditor)
        self.editorEdit.setObjectName(u"editorEdit")

        self.verticalLayout.addWidget(self.editorEdit)

        self.label = QLabel(PythonEditor)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.outputTextBrowser = QTextBrowser(PythonEditor)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")

        self.verticalLayout.addWidget(self.outputTextBrowser)


        self.retranslateUi(PythonEditor)

        QMetaObject.connectSlotsByName(PythonEditor)
    # setupUi

    def retranslateUi(self, PythonEditor):
        PythonEditor.setWindowTitle(QCoreApplication.translate("PythonEditor", u"PythonEditor", None))
        self.newButton.setText(QCoreApplication.translate("PythonEditor", u"New", None))
        self.openButton.setText(QCoreApplication.translate("PythonEditor", u"Open", None))
        self.saveButton.setText(QCoreApplication.translate("PythonEditor", u"Save", None))
        self.saveAsButton.setText(QCoreApplication.translate("PythonEditor", u"Save as", None))
        self.runButton.setText(QCoreApplication.translate("PythonEditor", u"\u57f7\u884c Run", None))
        self.filenameLabel.setText(QCoreApplication.translate("PythonEditor", u"filename.py", None))
        self.label.setText(QCoreApplication.translate("PythonEditor", u"Output", None))
        self.outputTextBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

