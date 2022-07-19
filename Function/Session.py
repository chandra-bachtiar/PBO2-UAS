import json
import os
import sys


def createSession(iduser, username, rolename,nama):
    # create file session in json and its hidden and set permission for all user
    file = open("session.json", "w")
    data = {
        "iduser": iduser,
        "username": username,
        "rolename": rolename,
        "nama": nama
    }
    json.dump(data, file)
    file.close()
    os.system("chmod -R 777 session.json")
    return True


def getSession():
    # get session from json
    if os.path.isfile("session.json"):
        file = open("session.json", "r")
        data = json.loads(file.read())
        file.close()
        return data
    else:
        return False


def clearSession():
    # clear session from json
    if os.path.isfile("session.json"):
        os.remove("session.json")
        return True
    else:
        return False


def getUser():
    # get iduser from session
    if os.path.isfile("session.json"):
        file = open("session.json", "r")
        data = json.loads(file.read())
        file.close()
        return data["iduser"]
    else:
        return False

def getNama():
    # get nama from session
    if os.path.isfile("session.json"):
        file = open("session.json", "r")
        data = json.loads(file.read())
        file.close()
        return data["nama"]
    else:
        return False

def getRole():
    # get rolename from session
    if os.path.isfile("session.json"):
        file = open("session.json", "r")
        data = json.loads(file.read())
        file.close()
        return data["rolename"]
    else:
        return False
