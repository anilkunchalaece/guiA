# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(640, 380)
        Login.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.groupBox = QtGui.QGroupBox(Login)
        self.groupBox.setGeometry(QtCore.QRect(120, 40, 371, 301))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.username_txt = QtGui.QLineEdit(self.groupBox)
        self.username_txt.setGeometry(QtCore.QRect(100, 50, 201, 31))
        self.username_txt.setInputMask(_fromUtf8(""))
        self.username_txt.setObjectName(_fromUtf8("username_txt"))
        self.pass_txt = QtGui.QLineEdit(self.groupBox)
        self.pass_txt.setGeometry(QtCore.QRect(100, 100, 201, 31))
        self.pass_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_txt.setObjectName(_fromUtf8("pass_txt"))
        self.loginBtn = QtGui.QPushButton(self.groupBox)
        self.loginBtn.setGeometry(QtCore.QRect(120, 220, 121, 41))
        self.loginBtn.setStyleSheet(_fromUtf8("font: 10pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(85, 170, 255);"))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.username_label = QtGui.QLabel(self.groupBox)
        self.username_label.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.pass_label = QtGui.QLabel(self.groupBox)
        self.pass_label.setGeometry(QtCore.QRect(20, 100, 71, 31))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
        self.pass_label_2 = QtGui.QLabel(self.groupBox)
        self.pass_label_2.setGeometry(QtCore.QRect(20, 150, 71, 31))
        self.pass_label_2.setObjectName(_fromUtf8("pass_label_2"))
        self.tid_txt = QtGui.QLineEdit(self.groupBox)
        self.tid_txt.setGeometry(QtCore.QRect(100, 150, 201, 31))
        self.tid_txt.setText(_fromUtf8(""))
        self.tid_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.tid_txt.setObjectName(_fromUtf8("tid_txt"))
        self.invalidLogin = QtGui.QLabel(self.groupBox)
        self.invalidLogin.setEnabled(False)
        self.invalidLogin.setGeometry(QtCore.QRect(10, 275, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.invalidLogin.setFont(font)
        self.invalidLogin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.invalidLogin.setText(_fromUtf8(""))
        self.invalidLogin.setObjectName(_fromUtf8("invalidLogin"))
        self.label = QtGui.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(500, 360, 141, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(0, 360, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Dialog", None))
        self.groupBox.setTitle(_translate("Login", "Login ", None))
        self.loginBtn.setText(_translate("Login", "LOGIN", None))
        self.username_label.setText(_translate("Login", "USERNAME :", None))
        self.pass_label.setText(_translate("Login", "PASSWORD :", None))
        self.pass_label_2.setText(_translate("Login", "TEST ID :", None))
        self.label.setText(_translate("Login", "@copyright by MEDPG.NET", None))
        self.label_2.setText(_translate("Login", " QB SMART Ver 1.0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

