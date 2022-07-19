import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))

import hashlib
from Main.db.database import DBConnection as mydb
class userRegister:
    def __init__(self):
        self.__nama = None
        self.__username= None
        self.__password= None
        self.__email= None
        self.__rolename= None
        self.__info = None
        self.__isRegistered = False
        self.conn = None
        self.affected = None
        self.result = None
    
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
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, value):
        self.__info = value
    
    @property
    def rolename(self):
        return self.__rolename

    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
    
    @property
    def isRegistered(self):
        return self.__isRegistered

    @isRegistered.setter
    def isRegistered(self, value):
        self.__isRegistered = value

    def checkUsername(self,username):
        user = str(username).lower()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE lower(username)='" + user + "'"
        # print(sql)
        self.result = self.conn.findOne(sql)
        # print(self.result)
        if(self.result!=None):
            self.__info = "Username sudah terdaftar"
            self.affected = self.conn.cursor.rowcount
            self.__isRegistered = True
        else:
            self.__info = "Username belum terdaftar"
            self.affected = self.conn.cursor.rowcount
            self.__isRegistered = False
        self.conn.disconnect
        return self.__isRegistered

    def registerUser(self):
        #check if username is already registered
        check = self.checkUsername(self.username)
        if(self.checkUsername(self.__username)):
            self.__info = "Username sudah terdaftar"
            return self.__info
        else:
            self.conn = mydb()
            sql="INSERT INTO users (nama, username, password, email, role) VALUES ('" + self.__nama + "','" + self.__username + "','" + self.__password + "','" + self.__email + "','" + self.__rolename + "')"
            self.result = self.conn.insert(sql)
            if(self.result):
                self.__info = "Berhasil mendaftar"
                self.__isRegistered = True
            else:
                self.__info = "Gagal mendaftar"
                self.__isRegistered = False
            self.conn.disconnect
            return self.__info

