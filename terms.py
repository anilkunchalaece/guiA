# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terms.ui'
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

class Ui_Terms(object):
    def setupUi(self, Terms):
        Terms.setObjectName(_fromUtf8("Terms"))
        Terms.resize(875, 612)
        self.textBrowser = QtGui.QTextBrowser(Terms)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 841, 391))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(Terms)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 410, 841, 91))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.checkBox = QtGui.QCheckBox(Terms)
        self.checkBox.setGeometry(QtCore.QRect(140, 540, 341, 41))
        self.checkBox.setStyleSheet(_fromUtf8("font: 75 12pt \"MS Shell Dlg 2\";"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton = QtGui.QPushButton(Terms)
        self.pushButton.setGeometry(QtCore.QRect(570, 530, 171, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.termsLabel = QtGui.QLabel(Terms)
        self.termsLabel.setGeometry(QtCore.QRect(140, 589, 521, 21))
        self.termsLabel.setText(_fromUtf8(""))
        self.termsLabel.setObjectName(_fromUtf8("termsLabel"))

        self.retranslateUi(Terms)
        QtCore.QMetaObject.connectSlotsByName(Terms)

    def retranslateUi(self, Terms):
        Terms.setWindowTitle(_translate("Terms", "Dialog", None))
        self.textBrowser.setHtml(_translate("Terms", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Read Instructions </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Try to click Buttons</span></p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("Terms", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Terms and Conditions</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">You must read and understnad Instructions</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">and accept the terms to Start the Exam</span></p></body></html>", None))
        self.checkBox.setText(_translate("Terms", "I accept the terms and conditions", None))
        self.pushButton.setText(_translate("Terms", "StartExam", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Terms = QtGui.QDialog()
    ui = Ui_Terms()
    ui.setupUi(Terms)
    Terms.show()
    sys.exit(app.exec_())

