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
time_limit = datetime.timedelta(days=1)


def backup():
    try:
        t1 = time_now
        source = 'c:\\Users\\ojaco\\Desktop'
        shutil.copytree(source, 'N:\\DTOPBACKUP%s' % (t1))

    except:
        pass


def backup_of_backup():
    os.chdir('N:\\')
    shutil.copytree('DTOPBACKUP%s' % (time_now), 'E:\\BCKPOFBCKP%s' % (time_now))


def remove_old_backups(location):
    os.chdir(location)
    path = location
    for f in os.listdir(path):
        if 'DTOPBACKUP' in f or 'BCKPOFBCKP' in f:  # run dir command from console : Windows Explorer lies and hides.....
            if os.stat(f).st_mtime < now:
                with open('log_removed_backups.txt', 'a', encoding='utf-8') as fd:
                    fd.write('Removed {} at {}'.format(f, datetime.datetime.now()))
                    fd.write('\n')

                    #os.chmod(f, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR | stat.S_IWGRP | stat.S_IXGRP)
                    send2trash.send2trash(f)

                    print('REMOVED {}'.format(f))


def empty_recycle_bin():
    shell.SHEmptyRecycleBin(0, None, 1)
    print('Recycle bin emptied')


backup()
time.sleep(10)
backup_of_backup()
time.sleep(20)
remove_old_backups('E:\\')
remove_old_backups('N:\\')
time.sleep(20)
empty_recycle_bin()
