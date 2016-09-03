# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'completed.ui'
#
# Created: Sat Sep  3 13:39:48 2016
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_testCompleted(object):
    def setupUi(self, testCompleted):
        testCompleted.setObjectName(_fromUtf8("testCompleted"))
        testCompleted.resize(400, 300)
        self.textBrowser = QtGui.QTextBrowser(testCompleted)
        self.textBrowser.setGeometry(QtCore.QRect(40, 70, 291, 111))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(testCompleted)
        QtCore.QMetaObject.connectSlotsByName(testCompleted)

    def retranslateUi(self, testCompleted):
        testCompleted.setWindowTitle(_translate("testCompleted", "Dialog", None))
        self.textBrowser.setHtml(_translate("testCompleted", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:12pt; font-weight:200; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time is Completed..</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For Your Results Please Visit : Prepare2Pg site </p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    testCompleted = QtGui.QDialog()
    ui = Ui_testCompleted()
    ui.setupUi(testCompleted)
    testCompleted.show()
    sys.exit(app.exec_())

