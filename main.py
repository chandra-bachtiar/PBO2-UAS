import sys
from PyQt5.QtWidgets import *
from Main.form.login.login import WindowLogin as login
import atexit

__author__ = 'Kelompok 7 TIF UMC'

def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True) 
    window = login()
    window.show()
    sys.exit(a.exec_())

main()