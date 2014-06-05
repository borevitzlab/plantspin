from ctypes import *
import sys
import random
from time import sleep
import os
import time
timestr = time.strftime("%D-%M-%Y")
print timestr
from datetime import datetime

target = raw_input('/Users/u5212257/Desktop/x/')
prefix = raw_input('Enter prefix: ')
os.chdir('/Users/u5212257/Desktop/x/')
allfiles = os.listdir(target)
for filename in allfiles:
        t = os.path.getmtime(ALM)
        v = datetime.datetime.fromtimestamp(t)
        x = v.strftime('%Y%m%d-%H%M%S')
        os.rename(filename)