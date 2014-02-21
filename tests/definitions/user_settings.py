from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import os


f = open('counter.txt', 'r')
i = f.read()
n = int(i) + 1
f = open('counter.txt', 'w')
s = str(n)
f.write(s)
count = n

username = 'Troy Mcclure'
email = 'weqatester%d@weebly.com' % count
print email
old_email = 'weqatester12@weebly.com'
print old_email
password = 'W33bly!-13'
sel_domain = "inttesting%d" % count
