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

#Script automatically creates today's folder for photo archive


timestr = time.strftime("%D-%M-%Y")
print timestr

newpath = r'/Users/u5212257/Desktop/timestr/'; 
if not os.path.exists('/Users/u5212257/Desktop/timestr/'): os.makedirs('/Users/u5212257/Desktop/timestr/')

