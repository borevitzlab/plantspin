#what is this program,
#what version
#Etc.

# Written by Jared
# Date

from ctypes import *
import sys
import random
from time import sleep
import os
import time
from datetime import datetime
import time, datetime, os
import shutil


# Get today's date as a datetime type
today = datetime.date.today()  

# Get string representation: YYYY-MM-DD
# From a datetime type.
todaystr = today.isoformat()   
print(todaystr)
try:
    os.mkdir(todaystr)
except:
    print("today's date forlder is already made")
    pass

try:
    os.mkdir(data)
except:
    print("today's data forlder is already made")
    pass

#shutil.move('/Users/u5212257/brachyspin/data/','/Users/u5212257/brachyspin/data/')

#Script automatically creates today's folder for Accession photo archive
newpath = r'/Users/u5212257/brachyspin/data/'; 
if not os.path.exists('/Users/u5212257/brachyspin/data/ALM-2/'): os.makedirs('/Users/u5212257/brachyspin/data/ALM-2')

# shutil.move('/Users/u5212257/brachyspin/data/', '/Users/u5212257/brachyspin/(todaystr)')

# newpath = r'/Users/u5212257/brachyspin/'; 