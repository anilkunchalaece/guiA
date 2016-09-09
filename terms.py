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
        Terms.resize(640, 480)
        self.textBrowser = QtGui.QTextBrowser(Terms)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 611, 371))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.checkBox = QtGui.QCheckBox(Terms)
        self.checkBox.setGeometry(QtCore.QRect(30, 410, 341, 41))
        self.checkBox.setStyleSheet(_fromUtf8("font: 75 12pt \"MS Shell Dlg 2\";"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton = QtGui.QPushButton(Terms)
        self.pushButton.setGeometry(QtCore.QRect(450, 390, 171, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Terms)
        QtCore.QMetaObject.connectSlotsByName(Terms)

    def retranslateUi(self, Terms):
        Terms.setWindowTitle(_translate("Terms", "Dialog", None))
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

