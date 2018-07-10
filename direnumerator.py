# Code by OJ 10-07-2018

####################################################################################################################################
# This script will inventarize the contents of a hard drive (changeable at 'tup_curdir = os.walk('i:\\'))'                         #
# and write the file / dir names to a txt file and then dump the contents into an Excel file (using openpyxl) whereafter a set of  #
# hyperlinks can be created to the files on disk.                                                                                  #
#                                                                                                                                  #
# A little formatting and one copy action is necessary before creating hyperlinks with the =Hyperlink(a1;b1)                       #
#                                                                                                                                  #
# The necessary Excel function for said formatting is detailed below for the Dutch language version I use.                         #
####################################################################################################################################

import os
from openpyxl import Workbook
os.chdir('n:\\')  # should be changed to another drive - will hold output files [1 text and one Excel]

tup_curdir = os.walk('m:\\')  # this is the drive we want to inventorize.

with open('dirsN.txt', 'w', encoding='utf-8') as fin:
    counter = 0
    for p, d, f in tup_curdir:
        for file in f:
            fullname = os.path.join(p, file)
            fin.write(fullname)
            #print('Copying {}'.format(fullname))
            fin.write('\n')
            counter += 1
print('There are {} files in the locations searched'.format(counter))


def new_excel():
    wb = Workbook()
    # acquire sheet
    ws1 = wb.active
    with open('dirsN.txt', 'r', encoding='utf-8') as fout:
        for y, i in enumerate(fout):
            if y == 0:
                y += 1
            ws1.cell(row=y, column=1).value = i.strip('"')  # debatable if .strip() is necessary

    wb.save('fess.xlsx') # change to desired name


new_excel()

# To format out quotation marks for creation of hyperlinks in Excel run = WISSEN.CONTROL(cell) and copy down Eng = Clean; you need two columns anyway for hyperlink+descript.
