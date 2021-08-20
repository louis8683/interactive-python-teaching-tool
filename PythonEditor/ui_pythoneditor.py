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
        PythonEditor.resize(973, 809)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PythonEditor.sizePolicy().hasHeightForWidth())
        PythonEditor.setSizePolicy(sizePolicy)
        PythonEditor.setMinimumSize(QSize(500, 500))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newButton.sizePolicy().hasHeightForWidth())
        self.newButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.newButton)

        self.openButton = QPushButton(PythonEditor)
        self.openButton.setObjectName(u"openButton")
        sizePolicy1.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy1)

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
        sizePolicy1.setHeightForWidth(self.lineByLineButton.sizePolicy().hasHeightForWidth())
        self.lineByLineButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineByLineButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.filenameLabel = QLabel(PythonEditor)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.verticalLayout_4.addWidget(self.filenameLabel)

        self.editorEdit = QTextEdit(PythonEditor)
        self.editorEdit.setObjectName(u"editorEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.editorEdit.sizePolicy().hasHeightForWidth())
        self.editorEdit.setSizePolicy(sizePolicy2)
        self.editorEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.editorEdit)

        self.label = QLabel(PythonEditor)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.outputTextBrowser = QTextBrowser(PythonEditor)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.outputTextBrowser.sizePolicy().hasHeightForWidth())
        self.outputTextBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.outputTextBrowser)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(PythonEditor)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.globalVarTableWidget = QTableWidget(PythonEditor)
        if (self.globalVarTableWidget.columnCount() < 3):
            self.globalVarTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.globalVarTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.globalVarTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.globalVarTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.globalVarTableWidget.setObjectName(u"globalVarTableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.globalVarTableWidget.sizePolicy().hasHeightForWidth())
        self.globalVarTableWidget.setSizePolicy(sizePolicy4)
        self.globalVarTableWidget.setMinimumSize(QSize(0, 0))
        self.globalVarTableWidget.horizontalHeader().setVisible(True)
        self.globalVarTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.globalVarTableWidget.horizontalHeader().setHighlightSections(True)
        self.globalVarTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.globalVarTableWidget.horizontalHeader().setStretchLastSection(True)
        self.globalVarTableWidget.verticalHeader().setVisible(False)
        self.globalVarTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.globalVarTableWidget)

        self.label_3 = QLabel(PythonEditor)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.localVarTableWidget = QTableWidget(PythonEditor)
        if (self.localVarTableWidget.columnCount() < 3):
            self.localVarTableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.localVarTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.localVarTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.localVarTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.localVarTableWidget.setObjectName(u"localVarTableWidget")
        self.localVarTableWidget.horizontalHeader().setStretchLastSection(True)
        self.localVarTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.localVarTableWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

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
        self.label_2.setText(QCoreApplication.translate("PythonEditor", u"Global Variables \u5168\u57df\u8b8a\u6578", None))
        ___qtablewidgetitem = self.globalVarTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PythonEditor", u"Name \u540d\u7a31", None));
        ___qtablewidgetitem1 = self.globalVarTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PythonEditor", u"Value \u503c", None));
        ___qtablewidgetitem2 = self.globalVarTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PythonEditor", u"Type \u578b\u5225", None));
        self.label_3.setText(QCoreApplication.translate("PythonEditor", u"Local Variables \u5340\u57df\u8b8a\u6578", None))
        ___qtablewidgetitem3 = self.localVarTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PythonEditor", u"Name \u540d\u7a31", None));
        ___qtablewidgetitem4 = self.localVarTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PythonEditor", u"Value \u503c", None));
        ___qtablewidgetitem5 = self.localVarTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PythonEditor", u"Type \u578b\u5225", None));
    # retranslateUi

