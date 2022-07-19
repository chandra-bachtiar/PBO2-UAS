import sys,os
sys.path.insert(0, os.path.dirname(os.path.realpath(__name__)))
# from Main.form.login.login import WindowLogin as login
# from Main.form.register.userRegister import userRegister as register
# from Main.dashboard.pekerja.pekerja import PekerjaWindow as pekerja
# from Main.dashboard.perusahaan.perusahaan import PerusahaanWindow as perusahaan


def login():
    from Main.form.login.login import WindowLogin as login
    a = login()
    return a

def register():
    from Main.form.register.formRegister import WindowRegister as register
    a = register()
    return a

def pekerja():
    from Main.dashboard.pekerja.pekerja import PekerjaWindow as pekerja
    a = pekerja()
    return a

def perusahaan():
    from Main.dashboard.perusahaan.perusahaan import PerusahaanWindow as perusahaan
    a = perusahaan()
    return a
    
    