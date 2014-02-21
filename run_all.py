from tests import *
import unittest
from threading import Thread
from time import sleep
import os
import glob

#This file should be ran if you are using sauce labs to test in parallel.

os.chdir("./tests")
fileslist = glob.glob('*_test.py')
j = 0
for i in fileslist:
    fileslist[j] = i.rstrip(".py")
    j += 1
#print fileslist

for i in fileslist:
    unittest.main(module = 'tests.' + i)
