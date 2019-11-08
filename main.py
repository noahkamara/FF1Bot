import os.path
import pickle

from selenium import webdriver

import FormulaDatabase
from DriversAndConstructors import GetDriversAndConstructors
from TeamGenerator import GenerateFrom


class AuthCred:
    def __init__(self, login, password):
        self.login = login
        self.password = password


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def login(login="", password=""):
    if not (os.path.isfile("authCred.pkl")):
        print("Enter your login Credentials:")
        login = input("Email:    ")
        password = input("Password: ")
        cred = AuthCred(login, password)
        save_obj(cred, "authCred")
    else:
        cred = load_obj("authCred")

    return cred.login, cred.password


# FormulaDatabase.insertDrivers(drivers)

if __name__ == '__main__':
    drivers, constructors = GetDriversAndConstructors(login()[0], login()[1], webdriver.Chrome())
    GenerateFrom(drivers, constructors)
    FormulaDatabase.insertDrivers(drivers)
