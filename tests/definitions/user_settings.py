from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import os

count = 21
username = 'Tester McTesterson'
email = 'tester%d@weebly.com' % count
old_email = 'tester18@weebly.com' 
password = "W33bly!-13"
sel_domain = "inttesting%d" % count
