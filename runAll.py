from tests import *
import unittest
from threading import Thread
from time import sleep
import os
import glob

os.chdir("./tests")
fileslist = glob.glob('*_test.py')
j=0
for i in fileslist:
    fileslist[j]=i.rstrip(".py")
    j+=1
#print fileslist

for i in fileslist:
    def a():
        unittest.main(module= 'tests.' + i)
    Thread(target=a).start()
    sleep(2)
