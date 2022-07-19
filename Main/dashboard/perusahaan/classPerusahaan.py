import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import hashlib
from Main.db.database import DBConnection as mydb
from Function.Session import *


class classPerusahaan:
    def __init__(self):
        self.__iduser = None
        self.__idLoker = None
        self.__posisi = None
        self.__gaji = None
        self.__pendidikan = None
        self.__status = 'Pending'

        self.__nama = None
        self.__tanggal = None
        self.__alamat = None
        self.__jenis = None
        self.__username = None
        self.__password = None
        self.__email = None

        self.conn = None
        self.affected = None
        self.result = None

    @property
    def iduser(self):
        return self.__iduser

    @property
    def idLoker(self):
        return self.__idLoker

    @property
    def posisi(self):
        return self.__posisi

    @posisi.setter
    def posisi(self, value):
        self.__posisi = value

    @property
    def pendidikan(self):
        return self.__pendidikan

    @pendidikan.setter
    def pendidikan(self, value):
        self.__pendidikan = value

    @property
    def gaji(self):
        return self.__gaji

    @gaji.setter
    def gaji(self, value):
        self.__gaji = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def jenis(self):
        return self.__jenis

    @jenis.setter
    def jenis(self, value):
        self.__jenis = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    def cariLoker(self, id):
        self.conn = mydb()
        sql = 'SELECT * FROM master_loker WHERE "idLoker"=' + str(id) 
        self.result = self.conn.findOne(sql)
        self.affected = self.conn.cursor.rowcount
        self.conn.disconnect
        return self.result
    
    def cariUser(self):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = 'SELECT "nama","tgl_didirikan","alamat","jenis_perusahaan","username","password","email" FROM public.users  WHERE "iduser"=' + str(self.__iduser)
        self.result = self.conn.findOne(sql)
        self.affected = self.conn.cursor.rowcount
        self.conn.disconnect
        return self.result
    
    def rubahUser(self):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__nama, self.__tanggal, self.__alamat, self.__jenis, self.__username, self.__password, self.__email, self.__iduser)
        sql = 'UPDATE users SET "nama" = %s, "tgl_didirikan"= %s, "alamat"=%s, "jenis_perusahaan"=%s, "username"=%s, "password"=%s, "email"=%s WHERE "iduser"=%s'
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def cariLokerSemua(self):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = '''
            SELECT a."idLoker",a."Posisi",a."Pendidikan",a."Gaji",
            (SELECT count("idDetail") from detail_loker where "idLoker" = a."idLoker")
            FROM master_loker a
            WHERE "idPerusahaan"=
        ''' + str(self.__iduser)
        self.result = self.conn.findAll(sql)
        self.conn.disconnect
        return self.result
    
    def cariPelamar(self):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = '''
            SELECT
            a."idDetail",users.nama,b."Posisi",users.pendidikan,a.status
            FROM detail_loker a
            inner join master_loker b on b."idLoker" = a."idLoker"
            inner join users ON users.iduser = a."idPelamar"
            where b."idPerusahaan" = ''' + str(self.__iduser) + '''
        '''
        self.result = self.conn.findAll(sql)
        self.conn.disconnect
        return self.result

    def tambahLoker(self):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__iduser, self.__posisi, self.__gaji, self.__pendidikan)
        sql = 'INSERT INTO public.master_loker("idPerusahaan", "Posisi", "Gaji", "Pendidikan") VALUES ' + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def rubahLoker(self, id):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__posisi, self.__pendidikan, self.__gaji, id)
        sql = 'UPDATE master_loker SET "Posisi" = %s, "Pendidikan"= %s, "Gaji"=%s WHERE "idLoker"=%s'
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def hapusLoker(self, id):
        self.conn = mydb()
        sql = 'DELETE FROM master_loker WHERE "idLoker"=' + str(id) 
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def terimaLamaran(self, id):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = "UPDATE detail_loker SET status = 'Diterima' WHERE " + '"idDetail"=' + str(id)
        self.affected = self.conn.updateOne(sql)
        self.conn.disconnect
        return self.affected

    def tolakLamaran(self, id):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__status, id)
        sql = "UPDATE detail_loker SET status = 'Ditolak' WHERE" + '"idDetail"=' + str(id)
        self.affected = self.conn.updateOne(sql)
        self.conn.disconnect
        return self.affected

    def rubahUser(self):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__nama, self.__tanggal, self.__alamat, self.__jenis,
               self.__username, self.__password, self.__email, self.__iduser)
        sql = "UPDATE users SET nama = %s, tgl_didirikan= %s, alamat=%s, jenis_perusahaan=%s, username=%s, password=%s, email=%s WHERE iduser=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
