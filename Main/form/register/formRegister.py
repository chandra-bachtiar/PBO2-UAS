import sys,os
import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QMessageBox
from Main.form.register.userRegister import userRegister as Register
qtcreator_file  = "GUI/register.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowRegister(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)     
        # Event Setup
        self.btnRegister.clicked.connect(self.app_register)
        
    def app_register(self):
        nama = self.frmNama.text()
        username = self.frmUser.text()
        password = self.frmPassword.text()
        confirm = self.frmConfirm.text()
        email = self.frmEmail.text()
        rolename = ''
        if(self.opPekerja.isChecked()):
            rolename = 'Pekerja'
        elif(self.opPerusahaan.isChecked()):
            rolename = 'Perusahaan'
        else:
            self.messagebox("ERROR", "Pilih salah satu")

        if(password!=confirm):
            self.messagebox("Info","Password tidak sama")
        else:
            usr = Register()
            usr.nama = nama
            usr.username = username
            usr.password = password
            usr.email = email
            usr.rolename = rolename
            usr.registerUser()
            if(usr.info == "Berhasil mendaftar"):
                self.messagebox("Info",usr.info)
                self.clearInput()
            else:
                self.messagebox("Info",usr.info)

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()
    
    def clearInput(self):
        self.frmNama.setText("")
        self.frmUser.setText("")
        self.frmPassword.setText("")
        self.frmConfirm.setText("")
        self.frmEmail.setText("")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowRegister() # load object window login
    # windash = WindowDashboard() # load object window dashboard    
    window.show() # Tampilkan window login
    usr = Register()
    sys.exit(app.exec_())