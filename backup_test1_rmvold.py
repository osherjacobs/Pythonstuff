import time
import datetime
import os
import os.path
import shutil
import stat
now = time.time()
old = now - (24 * 60 * 60)
time_now = int(time.time())
time_now = str(time_now)
time_limit = datetime.timedelta(days=1)


def backup():
    try:
        t1 = time_now
        source = 'c:\\Users\\ojaco\\Desktop'
        shutil.copytree(source, 'N:\\BCKP\\DTOPBACKUP%s' % (t1))

    except:
        pass


def backup_of_backup():
    os.chdir('N:\\BCKP')
    shutil.copytree('DTOPBACKUP%s' % (time_now), 'E:\\BCKPOFBCKP%s' % (time_now))


def remove_old_backups(location):
    os.chdir(location)
    path = location
    for f in os.listdir(path):
        if 'DTOPBACKUP' in f:  # run dir command from console : Windows Explorer lies and hides.....
            if os.stat(f).st_mtime < now - (60):
                with open('log_removed_backups.txt', 'a', encoding='utf-8') as fd:
                    fd.write('Removed {} at {}'.format(f, datetime.datetime.now()))
                    fd.write('\n')
                os.chmod(f, stat.S_IWRITE)
                print('REMOVING {}'.format(f))
                shutil.rmtree(f)


# backup()
# time.sleep(10)
# backup_of_backup()
# time.sleep(5)
remove_old_backups('E:\\')
# remove_old_backups('E:\\')
