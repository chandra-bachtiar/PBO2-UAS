import sys
import os
import psycopg2 as mc
sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from Main.dashboard.pekerja.classPekerja import classPekerja
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic, QtCore
from Function.Session import *

qtcreator_file = "GUI/main-pelamar.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class PekerjaWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        profile = QPixmap("GUI/image/profile.png")
        logo = QPixmap("GUI/image/logo.png")

        
        
        self.setupUi(self)
        self.label_image.setPixmap(profile)
        self.label_logo.setPixmap(logo)

        self.editMode = False

        #event
        self.btnSimpanUser.clicked.connect(self.simpanUser)
        self.btnLamar.clicked.connect(self.lamar)
        self.btnBatalkan.clicked.connect(self.batalLamar)

    def setWelcomeText(self):
        nama = getNama()
        self.labelWelcome.setText("Selamat Datang, "+ str(nama))


    def ambilLowongan(self):
        try:
            pkerja = classPekerja()

            # Get all
            result = pkerja.cariLokerSemua()
            self.tableLowongan.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableLowongan.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableLowongan.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data Pekerjaan")

    def lamar(self):
        try:
            pkerja = classPekerja()
            idLoker = self.idLoker.text()
            a = pkerja.daftarLoker(idLoker)
            if(a>0):
                self.messagebox("SUKSES", "Anda Berhasil Mendaftar")
                self.clear_entry(self) 
                self.ambilLowongan() 
                self.ambilLowonganDaftar()
            else:
                self.messagebox("GAGAL", "Gagal Mendaftar")
        except mc.Error as e:
            self.messagebox("ERROR", str(e))
    
    def batalLamar(self):
        try:
            pkerja = classPekerja()
            idLoker = self.idLokerDaftar.text()
            a = pkerja.batalLamar(idLoker)
            if(a>0):
                self.messagebox("SUKSES", "Pendaftaran Anda Berhasil Dibatalkan")
                self.clear_entry(self) 
                self.ambilLowongan() 
                self.ambilLowonganDaftar()
            else:
                self.messagebox("GAGAL", "Gagal Membatalkan Pendaftaran")
        except mc.Error as e:
            self.messagebox("ERROR", str(e))
    
    def ambilLowonganDaftar(self):
        try:
            pkerja = classPekerja()

            # Get all
            result = pkerja.cariLokerDaftar()
            self.tableDaftar.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableDaftar.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableDaftar.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data Pekerjaan")

    def cariLowongan(self):
        try:
            idLowongan = self.txtID.text()
            pkerja = classPekerja()
            result = pkerja.cariLoker(idLowongan)
            a = pkerja.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtID.setFocus()
                self.btnTambah.setText("Simpan")
                self.editMode=False
                self.btnHapus.setEnabled(False)
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    

    def batalkan(self, MainWindow):
        try:
            pkerja = classPekerja()
            idLoker=self.idLokerDaftar.text()
            if(self.editMode==True):
                a = pkerja.hapusLoker(idLoker)
                if(a>0):
                    self.messagebox("SUKSES", "Data Lowongan Berhasil Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Lowongan Gagal Dihapus")

                self.clear_entry(self) # Clear Entry Form
                self.ambilLowongan() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    
    def TampilData(self,result):
        self.txtPosisi.setText(result[2])
        self.txtGaji.setText(str(int(result[3])))
        self.txtPendidikan.setText(result[4])
        self.btnTambah.setText("Update")
        self.editMode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus

    def simpanUser(self, MainWindow):
        try:
            pkerja = classPekerja()
            nama = self.namaUser.text()
            tempat = self.tempatLahir.text()
            alamat = self.alamat.toPlainText()
            pendidikan = str(self.cmbPendidikan.currentText())
            namaSekolah = self.namaSekolah.text()
            username = self.username.text()
            password = self.password.text()
            email = self.email.text()
            tgl = self.tglLahir.date()
            tgl = tgl.toPyDate()


            pkerja.nama = nama
            pkerja.alamat = alamat
            pkerja.tempatLahir = tempat
            pkerja.pendidikan = pendidikan
            pkerja.namaSekolah = namaSekolah
            pkerja.username = username
            pkerja.password = password
            pkerja.email = email
            pkerja.tglLahir = tgl
            a = pkerja.rubahUser()
            if(a>0):
                self.messagebox("SUKSES", "Data User Berhasil Dirubah")
            else:
                self.messagebox("GAGAL", "Data User Gagal Dirubah")
           
        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def cariUser(self):
        try:
            pkerja = classPekerja()
            result = pkerja.cariUser()
            a = pkerja.affected
            if(a>0):
                self.tampilDataUser(result)
            else:
                self.messagebox("INFO", "Data User tidak ditemukan")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    
    def tampilDataUser(self,result):
        pendidikan = None
        tglLahir = None
        if(result[4] == None):
            pendidikan = "-"
        else:
            pendidikan = result[4]


        self.namaUser.setText(result[0])
        self.tempatLahir.setText(result[2])
        self.alamat.setText(result[3])
        self.cmbPendidikan.setCurrentText(pendidikan)
        self.namaSekolah.setText(result[5])
        self.username.setText(result[6])
        self.password.setText(result[7])
        self.email.setText(result[8])
        
        if(result[1] != None):
            tgl = result[1].strftime('%d-%m-%Y')
            qdate = QtCore.QDate.fromString(tgl, "dd-MM-yyyy")
            self.tglLahir.setDate(qdate)

    def clear_entry(self, MainWindow):
        self.idLoker.setText("")
        self.idLokerDaftar.setText("")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PekerjaWindow()
    window.show()
    # window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = PekerjaWindow()
    # window.show()
    # window.select_data()
