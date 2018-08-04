from win32com.shell import shell
import time
import datetime
import os
import os.path
import shutil
import stat
now = time.time()
import send2trash
old = now - (7 * (24 * 60 * 60))
time_now = int(time.time())
time_now = str(time_now)
t1 = time_now


def backup():
    if not os.path.isdir('N:\\'):

        print('Check that the drive has been decrypted + mounted! Program dialogue for decryption will open - decrypt and then run backup rog. again!')
        os.startfile('C:\\Users\\ojaco\\Desktop\\BITLOCKER_SCRIPTS\\dist\\whatever\\whatever.exe')

    try:
        os.chdir('N:\\')
        print('STARTING BACKUP 1 !')

        source = 'c:\\Users\\ojaco\\Desktop'
        shutil.make_archive('DTOPBACKUP%s' % (t1), 'zip', source)

    except:
        pass

    finally:
        print('BACKUP 1 PERFORMED !')


def backup_of_backup():
    print('STARTING BACKUP 2 !')
    if not os.path.isdir('N:\\'):
        if not os.path.isdir('E:\\'):
            print('Check that the drive has been decrypted + mounted! Program dialogue for decryption will open - decrypt and then run backup rog. again!')
            os.startfile('C:\\Users\\ojaco\\Desktop\\BITLOCKER_SCRIPTS\\dist\\whatever\\whatever.exe')

    os.chdir('N:\\')

    shutil.copy('DTOPBACKUP%s%s' % (t1, '.zip'), 'E:\\')
    print('BACKUP 2 PERFORMED !')


def empty_recycle_bin():
    print('Emptying Recycle bin')
    shell.SHEmptyRecycleBin(0, None, 1)
    print('Recycle bin emptied')
    time.sleep(1)


def remove_old_backups(location):
    os.chdir(location)
    path = location
    for f in os.listdir(path):
        if 'DTOPBACKUP' in f or 'BCKPOFBCKP' in f:  # run dir command from console : Windows Explorer lies and hides.....
            if os.stat(f).st_mtime < old:
                with open('log_removed_backups.txt', 'a', encoding='utf-8') as fd:
                    fd.write('Removed {} at {}'.format(f, datetime.datetime.now()))
                    fd.write('\n')

                    #os.chmod(f, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR | stat.S_IWGRP | stat.S_IXGRP)
                    send2trash.send2trash(f)

                    print('REMOVED {}'.format(f))

                    time.sleep(5)
                    empty_recycle_bin()


backup()
time.sleep(2)
backup_of_backup()
time.sleep(10)
remove_old_backups('E:\\')
remove_old_backups('N:\\')
