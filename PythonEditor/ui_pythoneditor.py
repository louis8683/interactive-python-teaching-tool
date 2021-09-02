# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mbp13.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_PythonEditor(object):
    def setupUi(self, PythonEditor):
        if not PythonEditor.objectName():
            PythonEditor.setObjectName(u"PythonEditor")
        PythonEditor.resize(1066, 853)
        PythonEditor.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(PythonEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(PythonEditor)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #D9D9D9;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-family: \"Calibri\";\n"
"	font-size: 16px;\n"
"	color: #969696;\n"
"	margin-left: 10px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	font-family: \"Calibri\";\n"
"	font-size: 16px;\n"
"	color: #969696;\n"
"	margin-left: 10px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolbarFrame = QFrame(self.mainFrame)
        self.toolbarFrame.setObjectName(u"toolbarFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbarFrame.sizePolicy().hasHeightForWidth())
        self.toolbarFrame.setSizePolicy(sizePolicy)
        self.toolbarFrame.setStyleSheet(u"")
        self.toolbarFrame.setFrameShape(QFrame.StyledPanel)
        self.toolbarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.toolbarFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.primaryButtonsFrame = QFrame(self.toolbarFrame)
        self.primaryButtonsFrame.setObjectName(u"primaryButtonsFrame")
        self.primaryButtonsFrame.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #D9D9D9;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	height: 30px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"\n"
"	background-color: #FFFFFF;\n"
"	font-family: \"Calibri\";\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #CCE8FF;\n"
"}\n"
"\n"
"QPushButton:pressed  { \n"
"	background-color: #008FFF; \n"
"}")
        self.primaryButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.primaryButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.primaryButtonsFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.newButton = QPushButton(self.primaryButtonsFrame)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/note_add_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newButton.setIcon(icon)
        self.newButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.newButton)

        self.openButton = QPushButton(self.primaryButtonsFrame)
        self.openButton.setObjectName(u"openButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/source_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openButton.setIcon(icon1)
        self.openButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.openButton)

        self.saveButton = QPushButton(self.primaryButtonsFrame)
        self.saveButton.setObjectName(u"saveButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/save_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.saveAsButton = QPushButton(self.primaryButtonsFrame)
        self.saveAsButton.setObjectName(u"saveAsButton")
        self.saveAsButton.setIcon(icon2)
        self.saveAsButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.saveAsButton)

        self.runButton = QPushButton(self.primaryButtonsFrame)
        self.runButton.setObjectName(u"runButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play_circle_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.runButton.setIcon(icon3)
        self.runButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.runButton)

        self.lineByLineButton = QPushButton(self.primaryButtonsFrame)
        self.lineByLineButton.setObjectName(u"lineByLineButton")
        self.lineByLineButton.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/playlist_play_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lineByLineButton.setIcon(icon4)
        self.lineByLineButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.lineByLineButton)


        self.horizontalLayout_5.addWidget(self.primaryButtonsFrame)

        self.horizontalSpacer = QSpacerItem(750, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lineByLineFrame = QFrame(self.toolbarFrame)
        self.lineByLineFrame.setObjectName(u"lineByLineFrame")
        self.lineByLineFrame.setStyleSheet(u"QFrame {\n"
"	max-width: 340px;\n"
"}")
        self.lineByLineFrame.setFrameShape(QFrame.StyledPanel)
        self.lineByLineFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.lineByLineFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.lastButton = QPushButton(self.lineByLineFrame)
        self.lastButton.setObjectName(u"lastButton")
        self.lastButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #D9D9D9;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	min-width: 32px;\n"
"	max-width: 32px;\n"
"	height: 30px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"\n"
"	background-color: #FFFFFF;\n"
"	font-family: \"Calibri\";\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #CCE8FF;\n"
"}\n"
"\n"
"QPushButton:pressed  { \n"
"	background-color: #008FFF; \n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/fast_rewind_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lastButton.setIcon(icon5)
        self.lastButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.lastButton)

        self.stepButton = QPushButton(self.lineByLineFrame)
        self.stepButton.setObjectName(u"stepButton")
        self.stepButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #D9D9D9;\n"
"	height: 30px;\n"
"	max-width: 90px;\n"
"	min-width: 90px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"\n"
"	background-color: #FFFFFF;\n"
"	font-family: \"Calibri\";\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed  { \n"
"	background-color: #008FFF; \n"
"}")

        self.horizontalLayout_4.addWidget(self.stepButton)

        self.nextButton = QPushButton(self.lineByLineFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #D9D9D9;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;	\n"
"	min-width: 32px;\n"
"	max-width: 32px;\n"
"	height: 30px;\n"
"	margin-left: 0px;\n"
"	margin-right: 20px;\n"
"\n"
"	background-color: #FFFFFF;\n"
"	font-family: \"Calibri\";\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #CCE8FF;\n"
"}\n"
"\n"
"QPushButton:pressed  { \n"
"	background-color: #008FFF; \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/fast_forward_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon6)
        self.nextButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.nextButton)

        self.stepSlider = QSlider(self.lineByLineFrame)
        self.stepSlider.setObjectName(u"stepSlider")
        self.stepSlider.setStyleSheet(u"QSlider {\n"
"	min-width: 50px;\n"
"	max-width: 150px;\n"
"}")
        self.stepSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.stepSlider)


        self.horizontalLayout_5.addWidget(self.lineByLineFrame)


        self.verticalLayout_2.addWidget(self.toolbarFrame)

        self.filenameLabel = QLabel(self.mainFrame)
        self.filenameLabel.setObjectName(u"filenameLabel")
        self.filenameLabel.setStyleSheet(u"QLabel {\n"
"	margin-left: 20px;\n"
"	color: #969696;\n"
"	min-height: 20px;\n"
"	max-height: 20px;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.filenameLabel)

        self.editorInfoFrame = QFrame(self.mainFrame)
        self.editorInfoFrame.setObjectName(u"editorInfoFrame")
        self.editorInfoFrame.setStyleSheet(u"QSplitter::handle {\n"
"	background-color: #CCCCCC;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"}")
        self.editorInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.editorInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.editorInfoFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 0, 10, 10)
        self.splitter = QSplitter(self.editorInfoFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(False)
        self.editorConsoleFrame = QFrame(self.splitter)
        self.editorConsoleFrame.setObjectName(u"editorConsoleFrame")
        self.editorConsoleFrame.setStyleSheet(u"")
        self.editorConsoleFrame.setFrameShape(QFrame.StyledPanel)
        self.editorConsoleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.editorConsoleFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.editorSplitter = QSplitter(self.editorConsoleFrame)
        self.editorSplitter.setObjectName(u"editorSplitter")
        self.editorSplitter.setStyleSheet(u"")
        self.editorSplitter.setOrientation(Qt.Vertical)
        self.editorSplitter.setHandleWidth(1)
        self.editorSplitter.setChildrenCollapsible(False)
        self.editorFrame = QFrame(self.editorSplitter)
        self.editorFrame.setObjectName(u"editorFrame")
        self.editorFrame.setStyleSheet(u"QFrame {\n"
"	border-radius: 20px;\n"
"	background-color: #FFFFFF;\n"
"	margin-bottom: 10px;\n"
"}")
        self.editorFrame.setFrameShape(QFrame.StyledPanel)
        self.editorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.editorFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 12, 5, 0)
        self.editorLineNoBrowser = QTextBrowser(self.editorFrame)
        self.editorLineNoBrowser.setObjectName(u"editorLineNoBrowser")
        self.editorLineNoBrowser.setStyleSheet(u"QTextBrowser {\n"
"\n"
"	min-width: 40px;\n"
"	max-width: 40px;\n"
"}")
        self.editorLineNoBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.editorLineNoBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.editorLineNoBrowser.setLineWrapMode(QTextEdit.NoWrap)
        self.editorLineNoBrowser.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.editorLineNoBrowser)

        self.editorEdit = QTextEdit(self.editorFrame)
        self.editorEdit.setObjectName(u"editorEdit")
        self.editorEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_6.addWidget(self.editorEdit)

        self.editorSplitter.addWidget(self.editorFrame)
        self.consoleFrame = QFrame(self.editorSplitter)
        self.consoleFrame.setObjectName(u"consoleFrame")
        self.consoleFrame.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"}")
        self.consoleFrame.setFrameShape(QFrame.StyledPanel)
        self.consoleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.consoleFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.consoleSplitter = QSplitter(self.consoleFrame)
        self.consoleSplitter.setObjectName(u"consoleSplitter")
        self.consoleSplitter.setStyleSheet(u"")
        self.consoleSplitter.setOrientation(Qt.Horizontal)
        self.consoleSplitter.setHandleWidth(1)
        self.consoleSplitter.setChildrenCollapsible(False)
        self.outputFrame = QFrame(self.consoleSplitter)
        self.outputFrame.setObjectName(u"outputFrame")
        self.outputFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 20px;\n"
"	margin-right: 10px;\n"
"}")
        self.outputFrame.setFrameShape(QFrame.StyledPanel)
        self.outputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.outputFrame)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.outputLabel = QLabel(self.outputFrame)
        self.outputLabel.setObjectName(u"outputLabel")

        self.verticalLayout_6.addWidget(self.outputLabel)

        self.outputSeparateLine = QFrame(self.outputFrame)
        self.outputSeparateLine.setObjectName(u"outputSeparateLine")
        sizePolicy.setHeightForWidth(self.outputSeparateLine.sizePolicy().hasHeightForWidth())
        self.outputSeparateLine.setSizePolicy(sizePolicy)
        self.outputSeparateLine.setStyleSheet(u"QFrame {\n"
"	background-color: #D9D9D9;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"	min-height: 1px;\n"
"	max-height: 1px;\n"
"}")
        self.outputSeparateLine.setFrameShape(QFrame.StyledPanel)
        self.outputSeparateLine.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.outputSeparateLine)

        self.outputTextFrame = QFrame(self.outputFrame)
        self.outputTextFrame.setObjectName(u"outputTextFrame")
        self.outputTextFrame.setStyleSheet(u"QFrame {\n"
"	margin: 0px;\n"
"}")
        self.outputTextFrame.setFrameShape(QFrame.StyledPanel)
        self.outputTextFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.outputTextFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.outputLineNoBrowser = QTextBrowser(self.outputTextFrame)
        self.outputLineNoBrowser.setObjectName(u"outputLineNoBrowser")
        self.outputLineNoBrowser.setStyleSheet(u"QTextBrowser {\n"
"	min-width: 40px;\n"
"	max-width: 40px;\n"
"}")
        self.outputLineNoBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputLineNoBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outputLineNoBrowser.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLineNoBrowser.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_8.addWidget(self.outputLineNoBrowser)

        self.outputBrowser = QTextBrowser(self.outputTextFrame)
        self.outputBrowser.setObjectName(u"outputBrowser")
        self.outputBrowser.setStyleSheet(u"QTextBrowser {\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;\n"
"}")
        self.outputBrowser.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_8.addWidget(self.outputBrowser)


        self.verticalLayout_6.addWidget(self.outputTextFrame)

        self.consoleSplitter.addWidget(self.outputFrame)
        self.inputFrame = QFrame(self.consoleSplitter)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 20px;\n"
"	margin-left: 10px;\n"
"}")
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.inputFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.inputLabel = QLabel(self.inputFrame)
        self.inputLabel.setObjectName(u"inputLabel")

        self.verticalLayout_5.addWidget(self.inputLabel)

        self.inputSeparateLine = QFrame(self.inputFrame)
        self.inputSeparateLine.setObjectName(u"inputSeparateLine")
        sizePolicy.setHeightForWidth(self.inputSeparateLine.sizePolicy().hasHeightForWidth())
        self.inputSeparateLine.setSizePolicy(sizePolicy)
        self.inputSeparateLine.setStyleSheet(u"QFrame {\n"
"	background-color: #D9D9D9;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"	min-height: 1px;\n"
"	max-height: 1px;\n"
"}")
        self.inputSeparateLine.setFrameShape(QFrame.StyledPanel)
        self.inputSeparateLine.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.inputSeparateLine)

        self.inputTextFrame = QFrame(self.inputFrame)
        self.inputTextFrame.setObjectName(u"inputTextFrame")
        self.inputTextFrame.setStyleSheet(u"QFrame {\n"
"	margin: 0px;\n"
"}")
        self.inputTextFrame.setFrameShape(QFrame.StyledPanel)
        self.inputTextFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.inputTextFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.inputLineNoBrowser = QTextBrowser(self.inputTextFrame)
        self.inputLineNoBrowser.setObjectName(u"inputLineNoBrowser")
        self.inputLineNoBrowser.setStyleSheet(u"QTextBrowser {\n"
"	min-width: 40px;\n"
"	max-width: 40px;\n"
"}")
        self.inputLineNoBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inputLineNoBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inputLineNoBrowser.setLineWrapMode(QTextEdit.NoWrap)
        self.inputLineNoBrowser.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_7.addWidget(self.inputLineNoBrowser)

        self.inputBrowser = QTextBrowser(self.inputTextFrame)
        self.inputBrowser.setObjectName(u"inputBrowser")
        self.inputBrowser.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_7.addWidget(self.inputBrowser)


        self.verticalLayout_5.addWidget(self.inputTextFrame)

        self.consoleSplitter.addWidget(self.inputFrame)

        self.verticalLayout_7.addWidget(self.consoleSplitter)

        self.editorSplitter.addWidget(self.consoleFrame)

        self.verticalLayout_3.addWidget(self.editorSplitter)

        self.splitter.addWidget(self.editorConsoleFrame)
        self.infoFrame = QFrame(self.splitter)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setStyleSheet(u"")
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.splitter_2 = QSplitter(self.infoFrame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(1)
        self.globalVarFrame = QFrame(self.splitter_2)
        self.globalVarFrame.setObjectName(u"globalVarFrame")
        self.globalVarFrame.setStyleSheet(u"")
        self.globalVarFrame.setFrameShape(QFrame.StyledPanel)
        self.globalVarFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.globalVarFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 5)
        self.globalVarLabelFrame = QFrame(self.globalVarFrame)
        self.globalVarLabelFrame.setObjectName(u"globalVarLabelFrame")
        self.globalVarLabelFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFF5C5;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;	\n"
"}")
        self.globalVarLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.globalVarLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.globalVarLabelFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.globalVarLabel = QLabel(self.globalVarLabelFrame)
        self.globalVarLabel.setObjectName(u"globalVarLabel")

        self.verticalLayout_16.addWidget(self.globalVarLabel)


        self.verticalLayout_9.addWidget(self.globalVarLabelFrame)

        self.globalVarTableFrame = QFrame(self.globalVarFrame)
        self.globalVarTableFrame.setObjectName(u"globalVarTableFrame")
        self.globalVarTableFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;	\n"
"}")
        self.globalVarTableFrame.setFrameShape(QFrame.StyledPanel)
        self.globalVarTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.globalVarTableFrame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.globalVarTable = QTableWidget(self.globalVarTableFrame)
        if (self.globalVarTable.columnCount() < 3):
            self.globalVarTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.globalVarTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.globalVarTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.globalVarTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.globalVarTable.rowCount() < 2):
            self.globalVarTable.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.globalVarTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.globalVarTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.globalVarTable.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.globalVarTable.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.globalVarTable.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.globalVarTable.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.globalVarTable.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.globalVarTable.setItem(1, 2, __qtablewidgetitem10)
        self.globalVarTable.setObjectName(u"globalVarTable")
        self.globalVarTable.setGridStyle(Qt.NoPen)
        self.globalVarTable.horizontalHeader().setStretchLastSection(True)
        self.globalVarTable.verticalHeader().setVisible(False)

        self.verticalLayout_15.addWidget(self.globalVarTable)


        self.verticalLayout_9.addWidget(self.globalVarTableFrame)

        self.splitter_2.addWidget(self.globalVarFrame)
        self.localVarFrame = QFrame(self.splitter_2)
        self.localVarFrame.setObjectName(u"localVarFrame")
        self.localVarFrame.setStyleSheet(u"")
        self.localVarFrame.setFrameShape(QFrame.StyledPanel)
        self.localVarFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.localVarFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 5, 0, 5)
        self.localVarLabelFrame = QFrame(self.localVarFrame)
        self.localVarLabelFrame.setObjectName(u"localVarLabelFrame")
        self.localVarLabelFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #DDF1B2;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;	\n"
"}")
        self.localVarLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.localVarLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.localVarLabelFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.localVarLabel = QLabel(self.localVarLabelFrame)
        self.localVarLabel.setObjectName(u"localVarLabel")

        self.verticalLayout_20.addWidget(self.localVarLabel)


        self.verticalLayout_10.addWidget(self.localVarLabelFrame)

        self.localVarTableFrame = QFrame(self.localVarFrame)
        self.localVarTableFrame.setObjectName(u"localVarTableFrame")
        self.localVarTableFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;	\n"
"}")
        self.localVarTableFrame.setFrameShape(QFrame.StyledPanel)
        self.localVarTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.localVarTableFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.localVarTable = QTableWidget(self.localVarTableFrame)
        if (self.localVarTable.columnCount() < 3):
            self.localVarTable.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.localVarTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.localVarTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.localVarTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.localVarTable.setObjectName(u"localVarTable")
        self.localVarTable.setGridStyle(Qt.NoPen)
        self.localVarTable.horizontalHeader().setStretchLastSection(True)
        self.localVarTable.verticalHeader().setVisible(False)

        self.verticalLayout_19.addWidget(self.localVarTable)


        self.verticalLayout_10.addWidget(self.localVarTableFrame)

        self.splitter_2.addWidget(self.localVarFrame)
        self.callStackFrame = QFrame(self.splitter_2)
        self.callStackFrame.setObjectName(u"callStackFrame")
        self.callStackFrame.setStyleSheet(u"")
        self.callStackFrame.setFrameShape(QFrame.StyledPanel)
        self.callStackFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.callStackFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 0)
        self.callStackLabelFrame = QFrame(self.callStackFrame)
        self.callStackLabelFrame.setObjectName(u"callStackLabelFrame")
        self.callStackLabelFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #C3F1F6;\n"
"	border-top-left-radius: 20px;\n"
"	border-top-right-radius: 20px;	\n"
"}")
        self.callStackLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.callStackLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.callStackLabelFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.callStackVarLabel = QLabel(self.callStackLabelFrame)
        self.callStackVarLabel.setObjectName(u"callStackVarLabel")

        self.verticalLayout_18.addWidget(self.callStackVarLabel)


        self.verticalLayout_8.addWidget(self.callStackLabelFrame)

        self.callStackTableFrame = QFrame(self.callStackFrame)
        self.callStackTableFrame.setObjectName(u"callStackTableFrame")
        self.callStackTableFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-bottom-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;	\n"
"}")
        self.callStackTableFrame.setFrameShape(QFrame.StyledPanel)
        self.callStackTableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.callStackTableFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.callStackTable = QTableWidget(self.callStackTableFrame)
        self.callStackTable.setObjectName(u"callStackTable")

        self.verticalLayout_17.addWidget(self.callStackTable)


        self.verticalLayout_8.addWidget(self.callStackTableFrame)

        self.splitter_2.addWidget(self.callStackFrame)

        self.verticalLayout_4.addWidget(self.splitter_2)

        self.splitter.addWidget(self.infoFrame)

        self.verticalLayout_13.addWidget(self.splitter)


        self.verticalLayout_2.addWidget(self.editorInfoFrame)


        self.verticalLayout.addWidget(self.mainFrame)


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
        self.lineByLineButton.setText(QCoreApplication.translate("PythonEditor", u"Line-by-Line", None))
        self.lastButton.setText("")
        self.stepButton.setText(QCoreApplication.translate("PythonEditor", u"999 / 999", None))
        self.nextButton.setText("")
        self.filenameLabel.setText(QCoreApplication.translate("PythonEditor", u"Filename: No file opened yet.", None))
        self.editorLineNoBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-family:'Consolas'; font-size:14pt;\">99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">12</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">13</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">14<"
                        "/span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">15</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">16</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">17</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">18</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">19</span></p>\n"
"<p style=\" margin-top:0px; ma"
                        "rgin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">21</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">22</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">23</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">24</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">25</span></p></body></html>", None))
        self.editorEdit.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1e1e1e;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">from</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">PySide6</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,"
                        "monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QtGui</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">import</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Con"
                        "solas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">from</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">PySide6</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QtWidgets</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">import</span><"
                        "span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QApplication</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QFrame</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QHBoxLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,m"
                        "onospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QLabel</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QMainWindow</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QPushButton</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium"
                        ",Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QSizePolicy</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QSpacerItem</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QWidget</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">from</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">ToolbarItem</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">import</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4"
                        "d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">ToolbarItem</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">from</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">resources_rc</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'"
                        "; font-size:14px; color:#c586c0;\">import</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> *</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">import</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace"
                        "'; font-size:14px; color:#4ec9b0;\">sys</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#569cd6;\">class</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">Toolbar</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospa"
                        "ce'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QWidget</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">    </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#569cd6;\">def</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Co"
                        "urier New,monospace'; font-size:14px; color:#dcdcaa;\">__init__</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">scale</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">=</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">1</span><span style=\" font-family:'Fira Code Medium,Co"
                        "nsolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">super</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">Toolbar</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-fam"
                        "ily:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">).</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">__init__</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-f"
                        "amily:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icons</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">: </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">list</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; col"
                        "or:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">str</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">] = [</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,mon"
                        "ospace'; font-size:14px; color:#ce9178;\">&quot;New&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/note_add_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family"
                        ":'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Open&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/source_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospa"
                        "ce,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Save&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira C"
                        "ode Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/save_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Save as&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monos"
                        "pace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/save_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Run&quot;</span><span style=\" font-f"
                        "amily:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/play_circle_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace';"
                        " font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Line-by-Line&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/playlist_play_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\""
                        ">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Last&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monos"
                        "pace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/fast_rewind_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            (</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;Next&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QIcon</span><span style="
                        "\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;:/icons/icons/fast_forward_black_24dp.svg&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        ]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-s"
                        "ize:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">: </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">dict</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monosp"
                        "ace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">str</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">ToolbarItem</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">] = {}</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier Ne"
                        "w,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#6a9955;\"># Setup H layout</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style="
                        "\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QHBoxLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">"
                        "        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">setSpacing</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consola"
                        "s,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style=\" font-family:'Fira Code Medium,Consolas"
                        ",Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">setContentsMargins</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">,</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">,</span><span style"
                        "=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">,</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">min_width</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\""
                        ">max_height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">for</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-si"
                        "ze:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">in</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Cons"
                        "olas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icons</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[:-</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">2</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">]:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Cou"
                        "rier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">] = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">ToolbarItem</span><span sty"
                        "le=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px"
                        "; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">scale</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,mo"
                        "nospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">addWidget</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium"
                        ",Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">])</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">min_width</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> += </span><span style=\""
                        " font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">].</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; col"
                        "or:#dcdcaa;\">width</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">max_height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">max</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier N"
                        "ew,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">max_height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consola"
                        "s,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">].</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">())</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Cons"
                        "olas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">addItem</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">("
                        "</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QSpacerItem</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">100</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">0</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospa"
                        "ce'; font-size:14px; color:#4ec9b0;\">QSizePolicy</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">Expanding</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QSizePolicy</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">Minimum</span><span style=\" font-family:'Fira Code Medium"
                        ",Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">for</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medi"
                        "um,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icon</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">in</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span "
                        "style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icons</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[-</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#b5cea8;\">2</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">:]:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">  "
                        "          </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">] = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier Ne"
                        "w,monospace'; font-size:14px; color:#4ec9b0;\">ToolbarItem</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">icon</span><span style=\" font-family:'Fira Code Medium,Cons"
                        "olas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">scale</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-famil"
                        "y:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">addWidget</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px;"
                        " color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">])</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">min_width</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier"
                        " New,monospace'; font-size:14px; color:#d4d4d4;\"> += </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">].</span><span style=\" font-family:'Fira Code Medium,Consolas"
                        ",Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">width</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">max_height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">max</span><span style=\" font"
                        "-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">max_height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">, </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">items</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; co"
                        "lor:#d4d4d4;\">[</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">name</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">].</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">())</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#6a9955;\"># Set dimensions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">margin</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,"
                        "Courier New,monospace'; font-size:14px; color:#b5cea8;\">10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">setFixedHeight</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Co"
                        "urier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">max_height</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">setMinimumWidth</span><span style=\" fon"
                        "t-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">min_width</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> + </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">margin</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> * </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">self</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px"
                        "; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">horizontalLayout</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">count</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">())</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#c586c0;\">if</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> __name__ == </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#ce9178;\">&quot;__main__&quot;</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">:    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">    </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,mo"
                        "nospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">app</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">QApplication</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">([])</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">    </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">toolbar</span><span style=\" font-family:'Fira Cod"
                        "e Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\"> = </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">Toolbar</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">    </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">toolbar</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\""
                        " font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">show</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">()</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">    </span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#4ec9b0;\">sys</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">exit</sp"
                        "an><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">(</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#9cdcfe;\">app</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">.</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#dcdcaa;\">exec</span><span style=\" font-family:'Fira Code Medium,Consolas,Courier New,monospace,Consolas,Courier New,monospace'; font-size:14px; color:#d4d4d4;\">())</span></p></body></html>", None))
        self.outputLabel.setText(QCoreApplication.translate("PythonEditor", u"OUTPUT", None))
        self.outputLineNoBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consol"
                        "as'; font-size:14pt;\">99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">12</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">13</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">14</span></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">15</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">16</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">17</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">18</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">19</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">21</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">22</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">23</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">24</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">25</span></p></body></html>", None))
        self.outputBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.inputLabel.setText(QCoreApplication.translate("PythonEditor", u"INPUT", None))
        self.inputLineNoBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consol"
                        "as'; font-size:14pt;\">99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">111</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">11</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">12</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">13</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">14</span></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">15</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">16</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">17</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">18</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">19</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">21</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">22</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">23</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">24</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-family:'Consolas'; font-size:14pt;\">25</span></p></body></html>", None))
        self.inputBrowser.setHtml(QCoreApplication.translate("PythonEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.globalVarLabel.setText(QCoreApplication.translate("PythonEditor", u"Global Variables", None))
        ___qtablewidgetitem = self.globalVarTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PythonEditor", u"Name", None));
        ___qtablewidgetitem1 = self.globalVarTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PythonEditor", u"Value", None));
        ___qtablewidgetitem2 = self.globalVarTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PythonEditor", u"Type", None));
        ___qtablewidgetitem3 = self.globalVarTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PythonEditor", u"New Row", None));
        ___qtablewidgetitem4 = self.globalVarTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PythonEditor", u"New Row", None));

        __sortingEnabled = self.globalVarTable.isSortingEnabled()
        self.globalVarTable.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.globalVarTable.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PythonEditor", u"name", None));
        ___qtablewidgetitem6 = self.globalVarTable.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PythonEditor", u"\"Louis\"", None));
        ___qtablewidgetitem7 = self.globalVarTable.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PythonEditor", u"str", None));
        ___qtablewidgetitem8 = self.globalVarTable.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PythonEditor", u"li", None));
        ___qtablewidgetitem9 = self.globalVarTable.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PythonEditor", u"[1,2,3,4,5,6,7,8,9,0]", None));
        ___qtablewidgetitem10 = self.globalVarTable.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PythonEditor", u"list", None));
        self.globalVarTable.setSortingEnabled(__sortingEnabled)

        self.localVarLabel.setText(QCoreApplication.translate("PythonEditor", u"Local Variables", None))
        ___qtablewidgetitem11 = self.localVarTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PythonEditor", u"Name", None));
        ___qtablewidgetitem12 = self.localVarTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PythonEditor", u"Value", None));
        ___qtablewidgetitem13 = self.localVarTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PythonEditor", u"Type", None));
        self.callStackVarLabel.setText(QCoreApplication.translate("PythonEditor", u"Function Call Stack", None))
    # retranslateUi

