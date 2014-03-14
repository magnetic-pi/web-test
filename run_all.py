import unittest
from time import sleep
import os
import glob
from subprocess import Popen

processes = []
os.chdir("./tests")
tests = glob.glob('*sauce_test.py')
for test in tests:
    processes.append(Popen('python %s' % test, shell=True))
 
for process in processes:
    process.wait()
