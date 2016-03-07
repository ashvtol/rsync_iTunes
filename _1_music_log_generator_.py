#import os, time
#files = sorted(os.listdir(path), key=lambda x: (os.path.getctime(os.path.join(path, x))),reverse=True)
#print("\n".join(files))
##/Users/Az/Music/iTunes/iTunes Media/Music/
##path = '/Users/Az/Desktop/test/'

## generate old music log

import os
import glob
import time
import sys
name = sys.argv[1];
ct = 0
olog = open('./olog','wb')
for filename in glob.glob('/Users/'+name+'/Music/iTunes/iTunes Media/Music/**/*.m*', recursive=True):
    name = filename
    ct = ct+1
    name = name.split('/')
    name = (name[-1] + '\n').encode('utf-8')
    olog.write(name)
#olog.write(('Total Songs = '+repr(ct) + " as of "+time.asctime()).encode('utf-8'))
print("***************************************AZ********************************************")
print('*            Total Songs = '+repr(ct) + " as of "+time.asctime() + " are logged            *");    
print('*    Note:Only the changes to the existing library will be pushed to your device    *');
print("*************************************************************************************")

olog.close()
