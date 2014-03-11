from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import os


f = open('counter.txt', 'r')
i = f.read()
count = int(i) + 1
f2 = open('counter.txt', 'w')
s = str(count)
f2.write(s)

username = 'Troy Mcclure'
email = 'weqatester%d@weebly.com' % count
password = 'W33bly!-13'
sel_domain = "inttesting%d" % count

reset_pw = "testing"
reset_conf = "testing"

email2 = 'weqatester-reset%d@weebly.com' % count
