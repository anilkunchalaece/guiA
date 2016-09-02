# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layoutV2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_prepare2Pg(object):
    def setupUi(self, prepare2Pg):
        prepare2Pg.setObjectName(_fromUtf8("prepare2Pg"))
        prepare2Pg.resize(1245, 760)
        prepare2Pg.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(prepare2Pg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 0, 902, 122))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.frame)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 0, 901, 101))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 110, 902, 62))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textBrowser = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(640, 0, 261, 61))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 0, 441, 61))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.pushButton_14 = QtGui.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 10, 40, 40))
        self.pushButton_14.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 75 italic 12pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 201, 61))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(50, 180, 901, 241))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.QuestionLabel = QtGui.QTextBrowser(self.frame_3)
        self.QuestionLabel.setGeometry(QtCore.QRect(0, 0, 901, 231))
        self.QuestionLabel.setObjectName(_fromUtf8("QuestionLabel"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(50, 420, 901, 211))
        self.frame_4.setStyleSheet(_fromUtf8(""))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.optARadioButton = QtGui.QRadioButton(self.frame_4)
        self.optARadioButton.setGeometry(QtCore.QRect(10, 20, 891, 41))
        self.optARadioButton.setObjectName(_fromUtf8("optARadioButton"))
        self.buttonGroup = QtGui.QButtonGroup(prepare2Pg)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.optARadioButton)
        self.optBRadioButton = QtGui.QRadioButton(self.frame_4)
        self.optBRadioButton.setGeometry(QtCore.QRect(10, 70, 891, 41))
        self.optBRadioButton.setObjectName(_fromUtf8("optBRadioButton"))
        self.buttonGroup.addButton(self.optBRadioButton)
        self.optCRadioButton = QtGui.QRadioButton(self.frame_4)
        self.optCRadioButton.setGeometry(QtCore.QRect(10, 120, 891, 41))
        self.optCRadioButton.setObjectName(_fromUtf8("optCRadioButton"))
        self.buttonGroup.addButton(self.optCRadioButton)
        self.optDRadioButton = QtGui.QRadioButton(self.frame_4)
        self.optDRadioButton.setGeometry(QtCore.QRect(10, 170, 891, 41))
        self.optDRadioButton.setObjectName(_fromUtf8("optDRadioButton"))
        self.buttonGroup.addButton(self.optDRadioButton)
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(970, 0, 271, 711))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 255);"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 180, 271, 181))
        self.frame_6.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 127);\n"
""))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.answerdBtn = QtGui.QPushButton(self.frame_6)
        self.answerdBtn.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.answerdBtn.setStyleSheet(_fromUtf8(""))
        self.answerdBtn.setObjectName(_fromUtf8("answerdBtn"))
        self.notVisited = QtGui.QPushButton(self.frame_6)
        self.notVisited.setGeometry(QtCore.QRect(10, 60, 40, 40))
        self.notVisited.setStyleSheet(_fromUtf8(""))
        self.notVisited.setObjectName(_fromUtf8("notVisited"))
        self.markedForReview = QtGui.QPushButton(self.frame_6)
        self.markedForReview.setGeometry(QtCore.QRect(130, 60, 40, 40))
        self.markedForReview.setStyleSheet(_fromUtf8(""))
        self.markedForReview.setObjectName(_fromUtf8("markedForReview"))
        self.notAnswerdBtn = QtGui.QPushButton(self.frame_6)
        self.notAnswerdBtn.setGeometry(QtCore.QRect(130, 10, 40, 40))
        self.notAnswerdBtn.setStyleSheet(_fromUtf8(""))
        self.notAnswerdBtn.setObjectName(_fromUtf8("notAnswerdBtn"))
        self.answeredAndMarkedForReview = QtGui.QPushButton(self.frame_6)
        self.answeredAndMarkedForReview.setGeometry(QtCore.QRect(10, 110, 40, 40))
        self.answeredAndMarkedForReview.setStyleSheet(_fromUtf8(""))
        self.answeredAndMarkedForReview.setObjectName(_fromUtf8("answeredAndMarkedForReview"))
        self.label_2 = QtGui.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(60, 120, 171, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(180, 10, 71, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(180, 60, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.scrollArea = QtGui.QScrollArea(self.frame_5)
        self.scrollArea.setGeometry(QtCore.QRect(0, 410, 271, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 229))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.submitBtn = QtGui.QPushButton(self.frame_5)
        self.submitBtn.setGeometry(QtCore.QRect(60, 640, 150, 46))
        self.submitBtn.setStyleSheet(_fromUtf8("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);"))
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))
        self.textEdit_8 = QtGui.QTextEdit(self.frame_5)
        self.textEdit_8.setGeometry(QtCore.QRect(0, 370, 271, 41))
        self.textEdit_8.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 0);"))
        self.textEdit_8.setReadOnly(True)
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.frame_5)
        self.textBrowser_4.setGeometry(QtCore.QRect(150, 0, 121, 171))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_6 = QtGui.QTextBrowser(self.frame_5)
        self.textBrowser_6.setGeometry(QtCore.QRect(0, 0, 151, 171))
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.reviewAndNextBtn = QtGui.QPushButton(self.centralwidget)
        self.reviewAndNextBtn.setGeometry(QtCore.QRect(50, 640, 211, 46))
        self.reviewAndNextBtn.setStyleSheet(_fromUtf8("\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);"))
        self.reviewAndNextBtn.setObjectName(_fromUtf8("reviewAndNextBtn"))
        self.clrResponseBtn = QtGui.QPushButton(self.centralwidget)
        self.clrResponseBtn.setGeometry(QtCore.QRect(360, 640, 150, 46))
        self.clrResponseBtn.setStyleSheet(_fromUtf8("\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);"))
        self.clrResponseBtn.setObjectName(_fromUtf8("clrResponseBtn"))
        self.saveAndNextBtn = QtGui.QPushButton(self.centralwidget)
        self.saveAndNextBtn.setGeometry(QtCore.QRect(780, 640, 150, 46))
        self.saveAndNextBtn.setStyleSheet(_fromUtf8("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);"))
        self.saveAndNextBtn.setObjectName(_fromUtf8("saveAndNextBtn"))
        prepare2Pg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(prepare2Pg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1245, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        prepare2Pg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(prepare2Pg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        prepare2Pg.setStatusBar(self.statusbar)

        self.retranslateUi(prepare2Pg)
        QtCore.QMetaObject.connectSlotsByName(prepare2Pg)

    def retranslateUi(self, prepare2Pg):
        prepare2Pg.setWindowTitle(_translate("prepare2Pg", "MainWindow", None))
        self.textBrowser_5.setHtml(_translate("prepare2Pg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#aa5500;\">EXAM TITLE</span></p></body></html>", None))
        self.textBrowser.setHtml(_translate("prepare2Pg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">TIME REMAINING : 00:00:00</span></p></body></html>", None))
        self.pushButton_14.setText(_translate("prepare2Pg", "(i)", None))
        self.textBrowser_3.setHtml(_translate("prepare2Pg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">QUESTION NO  :  1</span></p></body></html>", None))
        self.optARadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optBRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optCRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optDRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.answerdBtn.setText(_translate("prepare2Pg", "1", None))
        self.notVisited.setText(_translate("prepare2Pg", "3", None))
        self.markedForReview.setText(_translate("prepare2Pg", "4", None))
        self.notAnswerdBtn.setText(_translate("prepare2Pg", "2", None))
        self.answeredAndMarkedForReview.setText(_translate("prepare2Pg", "5", None))
        self.label_2.setText(_translate("prepare2Pg", "Answered", None))
        self.label_3.setText(_translate("prepare2Pg", "Not Visited", None))
        self.label_4.setText(_translate("prepare2Pg", "Answered and marked for review", None))
        self.label_5.setText(_translate("prepare2Pg", "Not Answered", None))
        self.label_6.setText(_translate("prepare2Pg", "Marked for Review", None))
        self.submitBtn.setText(_translate("prepare2Pg", "SUBMIT", None))
        self.textEdit_8.setHtml(_translate("prepare2Pg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LEGEND</span></p></body></html>", None))
        self.textBrowser_4.setHtml(_translate("prepare2Pg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">NAME :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#0055ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#0055ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#0055ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">Ht.No:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#0055ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#0055ff;\"><br /></p></body></html>", None))
        self.textBrowser_6.setHtml(_translate("prepare2Pg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">       </span></p></body></html>", None))
        self.reviewAndNextBtn.setText(_translate("prepare2Pg", "Mark For Review And Next", None))
        self.clrResponseBtn.setText(_translate("prepare2Pg", "Clear Response", None))
        self.saveAndNextBtn.setText(_translate("prepare2Pg", "Save And  Next", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    prepare2Pg = QtGui.QMainWindow()
    ui = Ui_prepare2Pg()
    ui.setupUi(prepare2Pg)
    prepare2Pg.show()
    sys.exit(app.exec_())

