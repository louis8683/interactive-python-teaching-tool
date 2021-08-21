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
        PythonEditor.resize(700, 550)
        PythonEditor.setMinimumSize(QSize(700, 550))
        self.verticalLayout_7 = QVBoxLayout(PythonEditor)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(PythonEditor)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newButton = QPushButton(self.frame_4)
        self.newButton.setObjectName(u"newButton")

        self.horizontalLayout_2.addWidget(self.newButton)

        self.openButton = QPushButton(self.frame_4)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout_2.addWidget(self.openButton)

        self.saveButton = QPushButton(self.frame_4)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.saveAsButton = QPushButton(self.frame_4)
        self.saveAsButton.setObjectName(u"saveAsButton")

        self.horizontalLayout_2.addWidget(self.saveAsButton)

        self.runButton = QPushButton(self.frame_4)
        self.runButton.setObjectName(u"runButton")

        self.horizontalLayout_2.addWidget(self.runButton)

        self.lineByLineButton = QPushButton(self.frame_4)
        self.lineByLineButton.setObjectName(u"lineByLineButton")

        self.horizontalLayout_2.addWidget(self.lineByLineButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.stepSlider = QSlider(self.frame_4)
        self.stepSlider.setObjectName(u"stepSlider")
        self.stepSlider.setOrientation(Qt.Horizontal)
        self.stepSlider.setTickPosition(QSlider.TicksBelow)
        self.stepSlider.setTickInterval(100)

        self.horizontalLayout_2.addWidget(self.stepSlider)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_3 = QFrame(PythonEditor)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(650, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(375, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filenameLabel = QLabel(self.frame)
        self.filenameLabel.setObjectName(u"filenameLabel")
        self.filenameLabel.setMinimumSize(QSize(0, 12))

        self.verticalLayout.addWidget(self.filenameLabel)

        self.editorEdit = QTextEdit(self.frame)
        self.editorEdit.setObjectName(u"editorEdit")
        self.editorEdit.setMinimumSize(QSize(0, 300))
        self.editorEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout.addWidget(self.editorEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 12))

        self.verticalLayout.addWidget(self.label_2)

        self.outputTextBrowser = QTextBrowser(self.frame)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTextBrowser.sizePolicy().hasHeightForWidth())
        self.outputTextBrowser.setSizePolicy(sizePolicy)
        self.outputTextBrowser.setMinimumSize(QSize(0, 50))
        self.outputTextBrowser.setMaximumSize(QSize(16777215, 50))
        self.outputTextBrowser.setBaseSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.outputTextBrowser)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 100))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.globalVarTableWidget = QTableWidget(self.frame_2)
        if (self.globalVarTableWidget.columnCount() < 3):
            self.globalVarTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.globalVarTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.globalVarTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.globalVarTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.globalVarTableWidget.setObjectName(u"globalVarTableWidget")
        self.globalVarTableWidget.horizontalHeader().setStretchLastSection(True)
        self.globalVarTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.globalVarTableWidget)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.localVarTableWidget = QTableWidget(self.frame_2)
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

        self.verticalLayout_3.addWidget(self.localVarTableWidget)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.retranslateUi(PythonEditor)

        QMetaObject.connectSlotsByName(PythonEditor)
    # setupUi

    def retranslateUi(self, PythonEditor):
        PythonEditor.setWindowTitle(QCoreApplication.translate("PythonEditor", u"Form", None))
        self.newButton.setText(QCoreApplication.translate("PythonEditor", u"New", None))
        self.openButton.setText(QCoreApplication.translate("PythonEditor", u"Open", None))
        self.saveButton.setText(QCoreApplication.translate("PythonEditor", u"Save", None))
        self.saveAsButton.setText(QCoreApplication.translate("PythonEditor", u"Save as", None))
        self.runButton.setText(QCoreApplication.translate("PythonEditor", u"Run", None))
        self.lineByLineButton.setText(QCoreApplication.translate("PythonEditor", u"Line-by-line", None))
        self.label_5.setText(QCoreApplication.translate("PythonEditor", u"Step", None))
        self.filenameLabel.setText(QCoreApplication.translate("PythonEditor", u"File: \u5c1a\u672a\u958b\u555f\u6a94\u6848", None))
        self.editorEdit.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">        self._python_path = &quot;C:\\\\Python39\\\\python.exe&quot; # C:\\\\Users\\\\Louis\\\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">        self._python_path = &quot;C:\\\\Python39\\\\python.exe&quot; # C:\\\\Users\\\\Louis\\\\        self._python_path = &quot;C:\\\\Python39\\\\python.exe&quot; # C:\\\\Users\\\\Louis\\\\</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("PythonEditor", u"Output", None))
        self.outputTextBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("PythonEditor", u"Global Variables \u5168\u57df\u8b8a\u6578", None))
        ___qtablewidgetitem = self.globalVarTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PythonEditor", u"Name \u540d\u7a31", None));
        ___qtablewidgetitem1 = self.globalVarTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PythonEditor", u"Value \u503c", None));
        ___qtablewidgetitem2 = self.globalVarTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PythonEditor", u"Type \u578b\u5225", None));
        self.label_4.setText(QCoreApplication.translate("PythonEditor", u"Local Variables \u5340\u57df\u8b8a\u6578", None))
        ___qtablewidgetitem3 = self.localVarTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PythonEditor", u"Name \u540d\u7a31", None));
        ___qtablewidgetitem4 = self.localVarTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PythonEditor", u"Value \u503c", None));
        ___qtablewidgetitem5 = self.localVarTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PythonEditor", u"Type \u578b\u5225", None));
    # retranslateUi

