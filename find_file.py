import os
import pprint

path = 'k:\\directory_of_drives'

os.chdir(path)

ui = input('Please enter filename: ').lower()

data_files = os.listdir(os.getcwd())

for file in data_files:
    with open(file, 'r', encoding='utf-8') as fd:
        for line in fd:
            if ui in line.lower():
                print(line)

# TODO ADD WHILE LOOP ETC... TKINTER INTERFACE
