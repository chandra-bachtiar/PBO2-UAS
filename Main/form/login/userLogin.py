import os, sys; sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))

import hashlib
from Main.db.database import DBConnection as mydb
from Function.Session import *

class userLogin:
    def __init__(self):
        self.__iduser= None
        self.__username= None
        self.__password= None
        self.__nama= None
        self.__email= None
        self.__rolename= None
        self.__info = None
        self.__loginvalid = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def iduser(self):
        return self.__iduser
    
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
    def rolename(self):
        return self.__rolename

    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
    
    @property
    def loginvalid(self):
        return self.__loginvalid

    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value
        
    def Validasi(self, username, password):
        a=str(username)
        b=a.strip()
        pwd=str(password).strip()

        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + b + "' and password='" + pwd + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__username = self.result[1]
            self.__password = self.result[2]
            self.__nama = self.result[3]
            self.__email = self.result[4]
            self.__rolename = self.result[5]
            self.affected = self.conn.cursor.rowcount
            self.__loginvalid = True

            createSession(self.__id,self.__nama,self.__rolename,self.__nama)
        else:
            self.__username = ''                  
            self.__password = ''
            self.__nama = ''
            self.__email = ''         
            self.__rolename = ''                  
            self.affected = 0
            self.__loginvalid = False
        self.conn.disconnect
        return self.__loginvalid

