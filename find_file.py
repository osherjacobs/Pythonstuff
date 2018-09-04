# Code by OJ 04-09-18
import os
import sys
import pickle

counter = 0

running = True

while running:
    ui = input('Please enter filename: [ to quit press "q" and then "Enter" ] ').lower()
    if ui == 'q':
        sys.exit()
    with open('dict_holder', 'rb') as fd:
        holder = pickle.load(fd)
        for item in holder:
            if ui in item.lower():
                counter +=1
                print(item)
        print('{} items with search term "{}" found'.format(counter, ui))

