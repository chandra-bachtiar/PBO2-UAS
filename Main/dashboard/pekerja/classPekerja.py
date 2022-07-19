import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
import hashlib
from Main.db.database import DBConnection as mydb
from Function.Session import *


class classPekerja:
    def __init__(self):
        self.__iduser = None
        self.__idLoker = None
        self.__posisi = None
        self.__gaji = None
        # self.__pendidikan = None
        self.__status = 'Pending'

        self.__nama = None
        self.__tempatLahir = None
        self.__tglLahir = None
        self.__alamat = None
        self.__jenis = None
        self.__pendidikan = None
        self.__namaSekolah = None
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
    def namaSekolah(self):
        return self.__namaSekolah

    @namaSekolah.setter
    def namaSekolah(self, value):
        self.__namaSekolah = value

    @property
    def tempatLahir(self):
        return self.__tempatLahir

    @tempatLahir.setter
    def tempatLahir(self, value):
        self.__tempatLahir = value

    @property
    def tglLahir(self):
        return self.__tglLahir

    @tglLahir.setter
    def tglLahir(self, value):
        self.__tglLahir = value

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
        sql = 'SELECT "nama","tgl_lahir","tempat_lahir","alamat","pendidikan","nama_sekolah","username","password","email" FROM public.users  WHERE "iduser"=' + str(self.__iduser)
        self.result = self.conn.findOne(sql)
        self.affected = self.conn.cursor.rowcount
        self.conn.disconnect
        return self.result
    
    def rubahUser(self):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__nama, self.__tglLahir, self.__alamat, self.__tempatLahir, self.__pendidikan, self.__namaSekolah, self.__username, self.__password, self.__email, self.__iduser)
        sql = 'UPDATE users SET "nama" = %s, "tgl_lahir"= %s, "alamat"=%s, "tempat_lahir"=%s,"pendidikan"=%s,"nama_sekolah"=%s, "username"=%s, "password"=%s, "email"=%s WHERE "iduser"=%s'
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def cariLokerSemua(self):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = '''
        select a."idLoker",a."Posisi",b."nama",a."Pendidikan",b."alamat",a."Gaji" 
        from master_loker a 
        inner join users b on b."iduser" = a."idPerusahaan"
        where a."idLoker" not in (
            select distinct "idLoker" 
            from detail_loker 
            where "idPelamar" = ''' + str(self.__iduser) + '''
        )
        '''
        self.result = self.conn.findAll(sql)
        self.conn.disconnect
        return self.result

    def cariLokerDaftar(self):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = '''
        select 
        a."idLoker",a."Posisi",c.nama,a."Pendidikan",c.alamat,a."Gaji",b.status
        from master_loker a
        inner join detail_loker b on b."idLoker" = a."idLoker"
        inner join users c on c.iduser = a."idPerusahaan"
        where b."idPelamar" = ''' + str(self.__iduser) + '''
        '''
        self.result = self.conn.findAll(sql)
        self.conn.disconnect
        return self.result

    def daftarLoker(self,id):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (id, self.__iduser, 'Pending')
        sql = 'INSERT INTO detail_loker("idLoker", "idPelamar", "status") VALUES ' + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def batalLamar(self,id):
        self.conn = mydb()
        self.__iduser = getUser()
        sql = 'DELETE FROM detail_loker where "idLoker"=' + str(id) + ' and "idPelamar"=' + str(self.__iduser)
        self.affected = self.conn.delete(sql)
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

    def terimaLoker(self, id):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__status, id)
        sql = "UPDATE detail_loker SET status = %s WHERE idDetail=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def tolakLoker(self, id):
        self.conn = mydb()
        self.__iduser = getUser()
        val = (self.__status, id)
        sql = "UPDATE detail_loker SET status = %s WHERE idDetail=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    # def rubahUser(self):
    #     self.conn = mydb()
    #     self.__iduser = getUser()
    #     val = (self.__nama, self.__tanggal, self.__alamat, self.__jenis,
    #            self.__username, self.__password, self.__email, self.__iduser)
    #     sql = "UPDATE users SET nama = %s, tgl_didirikan= %s, alamat=%s, jenis_perusahaan=%s, username=%s, password=%s, email=%s WHERE iduser=%s"
    #     self.affected = self.conn.update(sql, val)
    #     self.conn.disconnect
    #     return self.affected
