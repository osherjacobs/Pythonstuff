from tkinter import *

root = Tk()

root.title('Backup Application')
Label(text = 'BACKUP DESKTOP FOLDER TO N:\\Desktop').pack(pady = 15)

def quitapp():
    root.destroy()


def backup():
    import shutil
    source = 'c:\\users\\ojaco\\Desktop'
    dest = 'N:\\BACKUPDESKTOP'
    shutil.copytree(source, dest)
    for i in source:
        print("copying {}".format(source))


Button(text = 'BACKUP', command = backup).pack(side = LEFT)
Button(text = 'Quit', command = quitapp).pack(side = RIGHT)

root.mainloop()
