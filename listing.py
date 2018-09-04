# Code by OJ 04-09-18
import pickle
import os
import shutil
import win32api


hldr = []
dict_holder = {}

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

my_paths = drives


def main_search():
    
    for path in my_paths:
        for p, d, f in os.walk(path):
            for file in f:
                file_paths = os.path.join(p,file)
                hldr.append(file_paths)
                for  item in hldr:
                    dict_holder[item] = item
                    hldr.clear()
        with open('dict_holder', 'wb') as pickle_out:
            pickle.dump(dict_holder, pickle_out)
            #pickle_out.close()
                
                
main_search()
