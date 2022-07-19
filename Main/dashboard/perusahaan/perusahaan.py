import sys
import os
import psycopg2 as mc
sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
from Main.dashboard.perusahaan.classPerusahaan import classPerusahaan
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic, QtCore
from Function.Session import *

qtcreator_file = "GUI/main-perusahaan.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class PerusahaanWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        profile = QPixmap("GUI/image/profile.png")
        logo = QPixmap("GUI/image/logo.png")
        self.setupUi(self)
        self.label_image.setPixmap(profile)
        self.label_logo.setPixmap(logo)

        self.editMode = False

        nama = getNama()
        self.labelWelcome.setText("Selamat Datang, "+str(nama))

        #event
        self.btnSimpanUser.clicked.connect(self.simpanUser)
        self.btnHapus.clicked.connect(self.hapusLowongan)
        self.btnKosong.clicked.connect(self.clear_entry)
        self.btnTambah.clicked.connect(self.simpanLowongan) # ketika klik tombol submit
        self.btnCari.clicked.connect(self.cariLowongan)
        self.btnTerima.clicked.connect(self.terimaLamaran)
        self.btnTolak.clicked.connect(self.tolakLamaran)


    def ambilLowongan(self):
        try:
            comp = classPerusahaan()

            # Get all
            result = comp.cariLokerSemua()
            self.tableTambah.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableTambah.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableTambah.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data perusahaan")

    def cariLowongan(self):
        try:
            idLowongan = self.txtID.text()
            print(idLowongan)
            comp = classPerusahaan()
            result = comp.cariLoker(idLowongan)
            print(result)
            a = comp.affected
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

    def simpanLowongan(self, MainWindow):
        try:
            comp = classPerusahaan()
            posisi = self.txtPosisi.text()
            gaji = self.txtGaji.text()
            pendidikan = self.txtPendidikan.text()

            if(self.editMode==False):
                comp.posisi = posisi
                comp.gaji = gaji
                comp.pendidikan = pendidikan
                a = comp.tambahLoker()
                if(a>0):
                    self.messagebox("SUKSES", "Data Lowongan Berhasil Ditambahkan")
                    self.clear_entry(self) # Clear Entry Form
                    self.ambilLowongan() # Reload Datagrid
                else:
                    self.messagebox("GAGAL", "Data Lowongan Gagal Ditambahkan")

            elif(self.editMode==True):
                comp.posisi = posisi
                comp.gaji = gaji
                comp.pendidikan = pendidikan
                idLoker = self.txtID.text()
                a = comp.rubahLoker(idLoker)
                if(a>0):
                    self.messagebox("SUKSES", "Data Lowongan Berhasil Dirubah")
                    self.btnTambah.setText("Simpan")
                    self.editMode = False
                else:
                    self.messagebox("GAGAL", "Data Lowongan Gagal Dirubah")

                self.clear_entry(self) # Clear Entry Form
                self.ambilLowongan() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def hapusLowongan(self, MainWindow):
        try:
            comp = classPerusahaan()
            idLoker=self.txtID.text()
            print(idLoker)
            if(self.editMode==True):
                a = comp.hapusLoker(idLoker)
                if(a>0):
                    self.messagebox("SUKSES", "Data Lowongan Berhasil Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Lowongan Gagal Dihapus")

                self.clear_entry(self) # Clear Entry Form
                self.ambilLowongan() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")\
    
    def terimaLamaran(self):
        try:
            comp = classPerusahaan()
            idLoker=self.idDetail.text()
            print(idLoker)
            a = comp.terimaLamaran(idLoker)
            print(a)
            if(a>0):
                self.messagebox("SUKSES", "Data Lamaran Berhasil Diterima")
            else:
                self.messagebox("GAGAL", "Data Lamaran Gagal Diterima")

            self.clear_entry(self) # Clear Entry Form
            self.ambilPelamar() # Reload Datagrid
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")
    
    def tolakLamaran(self):
        try:
            comp = classPerusahaan()
            idLoker=self.idDetail.text()
            a = comp.tolakLamaran(idLoker)
            if(a>0):
                self.messagebox("SUKSES", "Data Lamaran Berhasil Ditolak")
            else:
                self.messagebox("GAGAL", "Data Lamaran Gagal Ditolak")

            self.clear_entry(self) # Clear Entry Form
            self.ambilPelamar() # Reload Datagrid
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    
    def ambilPelamar(self):
        try:
            comp = classPerusahaan()

            # Get all
            result = comp.cariPelamar()
            self.tablePelamar.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tablePelamar.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tablePelamar.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data perusahaan")

    
    def TampilData(self,result):
        self.txtPosisi.setText(result[2])
        self.txtGaji.setText(str(int(result[3])))
        self.txtPendidikan.setText(result[4])
        self.btnTambah.setText("Update")
        self.editMode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus

    def simpanUser(self, MainWindow):
        try:
            comp = classPerusahaan()
            nama = self.namaPerusahaan.text()
            alamat = self.alamat.toPlainText()
            jenisPerusahaan = self.jenisPerusahaan.text()
            username = self.username.text()
            password = self.password.text()
            email = self.email.text()
            tgl = self.tglDidirikan.date()
            tgl = tgl.toPyDate()


            comp.nama = nama
            comp.alamat = alamat
            comp.jenis = jenisPerusahaan
            comp.username = username
            comp.password = password
            comp.email = email
            comp.tanggal = tgl
            a = comp.rubahUser()
            if(a>0):
                self.messagebox("SUKSES", "Data User Berhasil Dirubah")
            else:
                self.messagebox("GAGAL", "Data User Gagal Dirubah")
           
        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def cariUser(self):
        try:
            comp = classPerusahaan()
            result = comp.cariUser()
            a = comp.affected
            if(a>0):
                self.tampilDataUser(result)
            else:
                self.messagebox("INFO", "Data User tidak ditemukan")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    
    def tampilDataUser(self,result):
        self.namaPerusahaan.setText(result[0])
        self.alamat.setText(result[2])
        self.jenisPerusahaan.setText(result[3])
        self.username.setText(result[4])
        self.password.setText(result[5])
        self.email.setText(result[6])
        
        if(result[1] != None):
            tgl = result[1].strftime('%d-%m-%Y')
            qdate = QtCore.QDate.fromString(tgl, "dd-MM-yyyy")
            self.tglDidirikan.setDate(qdate)

    def clear_entry(self, MainWindow):
        self.btnTambah.setText("Simpan")
        self.txtID.setText("")
        self.txtPosisi.setText("")
        self.txtPendidikan.setText("")
        self.txtGaji.setText("")
        self.idDetail.setText("")
        self.btnHapus.setEnabled(False)

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PerusahaanWindow()
    window.show()
    # window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = PerusahaanWindow()
    # window.show()
    # window.select_data()
