import os
import string
import shutil

import win32api

drives = win32api.GetLogicalDriveStrings()
drives=drives.split('\000')[:-1]


#os.chdir('k:\\')

my_paths = drives



def main_search():
    path = 'k:\\directory_of_drives'

    os.chdir('k:\\')
    if os.path.exists(path):
        shutil.rmtree(path)
        
    os.mkdir(path)
    os.chdir(path)
    counter = 0
    for path in my_paths:
        pathname = path[0]
        with open('{}_drive_files.txt'.format(pathname), 'w', encoding='utf-8') as fd:
            for p,d,f in os.walk(path):
                for file in f:
                    counter +=1
                    comp_path = os.path.join(p,file)
                    fd.write(comp_path +''+'\n')
    with open('report.txt', 'w', encoding='utf-8') as fd:
        fd.write('{} files registered from {} drives \n'.format(counter, len(drives)))

    
    

main_search()

with open('report.txt', 'a', encoding='utf-8') as fd:
        for i in os.listdir(os.getcwd()):
            i = os.path.abspath(i)
            fd.write(i+ ' ' + '\n')
