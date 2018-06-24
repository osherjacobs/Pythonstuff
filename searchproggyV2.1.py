# SEARCH PROGGIE
# AUTHOR: O. Jacobs (04-06-17)

import os
import subprocess


def one_drive_search():
    x = input("Please enter a path : ")
    search_term = input('Please enter a search term: ')
    counter = 0
    y = x +':\\'
    for p, d, f in os.walk(y):
        for f in f:
            if search_term in f.lower():
                print(os.path.join(p, f))
                counter+=1
    print ('-'*20,"Search finished",'-'*20)
    print("There are %d results" % counter)
    
                                   
def whole_system_search():
    my_paths = ['c:\\','e:\\','g:\\','h:\\','i:\\','j:\\', 'k:\\','l:\\','m:\\','n:\\','o:\\','z:\\']
    search_term = input('Please enter a search term: ')
    counter = 0
    for path in my_paths:
        for p, d, f in os.walk(path):
            for f in f:
                if search_term in f.lower():
                    print(os.path.join(p, f))
                    counter+=1
    print ('-'*20,"Search finished",'-'*20)
    print("There are %d results" % counter)
    
                    
#MAIN PROGRAM
def search_main():
    quest_1 = True
    while quest_1:
        
        driveStr = subprocess.check_output("fsutil fsinfo drives")
        #driveStr = driveStr.strip().lstrip('Drives: ')
        #drives = driveStr.split()
        my_paths = ['Drives on system:  c:\\','e:\\','g:\\','h:\\','i:\\','j:\\', 'k:\\','l:\\','m:\\','n:\\','o:\\ (may be encrypted: decrypt before searching!)']
        print(driveStr)
        quest_1 = input("System search or just one drive? \n 1. for one drive: \n 2. for system search:  \n 3. or press 'q' to quit :  ").lower()
        
        if quest_1 == '1':
            one_drive_search()
        if quest_1 == '2':
            whole_system_search()
        if quest_1  == 'q':
            quest_1 = False
            print('Program quitting! Bye!')
            break
    else:
        print('\nInvalid choice. Run the program again !\n')

search_main()
	



