import sys
import webbrowser


if(''.join(sys.argv[1:])) == '':
    print('Please enter web address!')
    sys.exit()
if len(sys.argv) > 0:
    webbrowser.open('https://www.' + ''.join(sys.argv[1:]))


# print(sys.argv[0])
