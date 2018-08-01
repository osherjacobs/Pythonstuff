

for file in i:
    stamp_file = (os.stat(file).st_mtime)
    stamp_file = int(stamp_file)
    stamp_file = time.gmtime(stamp_file)
    fmt = "%d-%m-%Y %H:%M:%S"
    timobj = time.strftime(fmt, stamp_file)
    print(file, timobj)

# Recursive 'os.walk(DRIVE)' version:

for p,d,f in os.walk('M:\\'):
	for file in f:
	        file = os.path.join(p,file)
	        stamp_file = (os.stat(file).st_mtime)
	        stamp_file = int(stamp_file)
	        stamp_file = time.gmtime(stamp_file)
	        timobj = time.strftime(fmt, stamp_file)
	        
	        with open('file_details.txt', 'a', encoding='utf-8') as fd:
	            fd.write(file )
	            fd.write("  TIMESTAMP: ")
	            fd.write(timobj)
	            fd.write('\n')
