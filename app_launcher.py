# Code by O. Jacobs
import datetime
import os
import logging

logging.basicConfig(filename='applauncher.log', level=logging.DEBUG)

cont = True

while cont:
    print '''#######OJ'S APP LAUNCHER #######

    Please enter the corresponding number to launch the program below :
    1.  Newsleecher
    2.  Google Chrome
    3.  Spotlite
    4.  Winamp
    5.  Administrative tools
    6.  Event viewer
    7.  CCleaner
    8.  VLC Player
    9.  RDP (Remote Desktop)
    10. CMD Shell
    11. Virtual Box
    12. Python 2.7.13 (IDLE)
    13. Python 3.6 (IDLE)
    14. OJ's search proggie

    '''
    x = input('>>>: ')
    path_1 = 'C:\\Program Files (x86)\\NewsLeecher\\newsleecher.exe'
    path_2 = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    path_3 = 'C:\\Program Files (x86)\\SpotLite\\Spotlite.exe'
    path_4 = 'C:\\Program Files (x86)\\Winamp\\winamp.exe'
    path_5 = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\Computer Management'
    path_6 = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\Event viewer'
    path_7 = 'C:\\Program Files\\CCleaner\\CCleaner64.exe'
    path_8 = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
    path_9 = 'C:\\WINDOWS\\system32\\mstsc.exe'
    path_10 = 'C:\\WINDOWS\\system32\\cmd.exe'
    path_11 = 'C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'
    path_12 = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 2.7\\IDLE (Python GUI)'
    path_13 = 'C:\\Python\\Python36\\Lib\\idlelib\\idle.pyw'
    path_14 = 'C:\\Users\\ojaco\\Desktop\\PYTHONDADDYFOLDER\\searchproggyV1.0.py'


    y = {
        1: path_1,
        2: path_2,
        3: path_3,
        4: path_4,
        5: path_5,
        6: path_6,
        7: path_7,
        8: path_8,
        9: path_9,
        10: path_10,
        11: path_11,
        12: path_12,
        13: path_13,
        14: path_14,
    }

    proggie = ''

    if x in y:

        proggie = y[x]
        os.startfile(proggie)
        logging.debug('launched {} at {}'.format(proggie, datetime.datetime.now()))

    time = datetime.datetime.now()
    formatted_time = time.strftime("%d/%B/%Y  %H:%M:%S")
    print "launched {} on / at {}".format(proggie, formatted_time)
    if x not in y:
        print '\n\t INVALID SELECTION: TRY AGAIN !! \n\t'
