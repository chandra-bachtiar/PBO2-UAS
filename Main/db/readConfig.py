import configparser

def readDB():
    # reading the env file
    config = configparser.ConfigParser()
    config.read('Main/db/.env')
    return config