#!py -3.6

import webbrowser
import sys
import pyperclip


#base_url = 'https://www.google.com/maps/place/'


if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
