for file in i:
    stamp_file = (os.stat(file).st_mtime)
    stamp_file = int(stamp_file)
    stamp_file = time.gmtime(stamp_file)
    timobj = time.strftime(fmt, stamp_file)
    print(file, timobj)
