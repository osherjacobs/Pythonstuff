import os

from shutil import copyfile

os.chdir("C:\\Users\\ojaco\\AppData\\Roaming\\vlc")

os.remove('vlc-qt-interface.ini')

os.chdir("C:\\Users\\ojaco\\AppData\\Roaming\\vlc\\backupinterfaceini")

copyfile('backupinterfaceini' , "C:\\Users\\ojaco\\AppData\\Roaming\\vlc")


