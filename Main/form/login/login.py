import os
import atexit
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from Function.Session import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtCore, uic
from Main.form.login.userLogin import userLogin as Login
from Main.form.register.formRegister import WindowRegister as Register
from Main.dashboard.perusahaan.perusahaan import PerusahaanWindow
from Main.dashboard.pekerja.pekerja import PekerjaWindow
# from FrmDashboard import WindowDashboard

qtcreator_file = "GUI/login.ui"  # File Design Tampilan Dashboard
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowLogin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Event Setup
        # ketika klik tombol submit
        self.btnLogin.clicked.connect(self.app_login)
        self.frmUser.returnPressed.connect(self.frmPassword.setFocus)
        self.frmPassword.returnPressed.connect(self.btnLogin.click)
        self.btnRegister.clicked.connect(self.register)

    def register(self):
        window.hide()
        winRegister.show()

    def app_login(self):
        username = self.frmUser.text()
        password = self.frmPassword.text()
        valid = usr.Validasi(username, password)
        if(valid == True):  # Login berhasil
            window.hide()
            #get role in session.json
            role = getRole()
            if(role == "Perusahaan"):
                winPerusahaan.show()
                winPerusahaan.ambilLowongan()
                winPerusahaan.cariUser()
                winPerusahaan.ambilPelamar()
            elif(role == "Pekerja"):
                winPekerja.show()
                winPekerja.setWelcomeText()
                winPekerja.ambilLowongan()
                winPekerja.ambilLowonganDaftar()
                winPekerja.cariUser()

                # self.messagebox("Info", f"Login Berhasil \n Selamat datang")
            
        else: 
            self.messagebox("Info", "Maaf login gagal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


def exit_handler():
    # delete session
    clearSession()


atexit.register(exit_handler)
app = QtWidgets.QApplication(sys.argv)
usr = Login()
window = WindowLogin()
window.show()
winRegister = Register()
winPerusahaan = PerusahaanWindow()
winPekerja = PekerjaWindow()
sys.exit(app.exec_())
