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
        PythonEditor.resize(469, 407)
        self.verticalLayout = QVBoxLayout(PythonEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.lineByLineButton = QPushButton(PythonEditor)
        self.lineByLineButton.setObjectName(u"lineByLineButton")

        self.horizontalLayout.addWidget(self.lineByLineButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.filenameLabel = QLabel(PythonEditor)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.verticalLayout_4.addWidget(self.filenameLabel)

        self.editorEdit = QTextEdit(PythonEditor)
        self.editorEdit.setObjectName(u"editorEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorEdit.sizePolicy().hasHeightForWidth())
        self.editorEdit.setSizePolicy(sizePolicy)
        self.editorEdit.setMinimumSize(QSize(0, 20))

        self.verticalLayout_4.addWidget(self.editorEdit)

        self.label = QLabel(PythonEditor)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.outputTextBrowser = QTextBrowser(PythonEditor)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outputTextBrowser.sizePolicy().hasHeightForWidth())
        self.outputTextBrowser.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.outputTextBrowser)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.globalVarTableWidget = QTableWidget(PythonEditor)
        self.globalVarTableWidget.setObjectName(u"globalVarTableWidget")

        self.verticalLayout_5.addWidget(self.globalVarTableWidget)

        self.localVarTableWidget = QTableWidget(PythonEditor)
        self.localVarTableWidget.setObjectName(u"localVarTableWidget")

        self.verticalLayout_5.addWidget(self.localVarTableWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


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
        self.lineByLineButton.setText(QCoreApplication.translate("PythonEditor", u"\u9010\u884c\u57f7\u884c", None))
        self.filenameLabel.setText(QCoreApplication.translate("PythonEditor", u"No file opened yet.", None))
        self.label.setText(QCoreApplication.translate("PythonEditor", u"Output", None))
        self.outputTextBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
    # retranslateUi

