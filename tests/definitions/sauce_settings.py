from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import os


baseUrl = "http://www.weebly.com"
waitTime = 20

desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
desired_capabilities['version'] = '27'
desired_capabilities['platform'] = 'Linux'
desired_capabilities['name'] = 'Testing Weebly Registration.'

driver = webdriver.Remote(
    desired_capabilities=desired_capabilities,
    command_executor="http://jcostellowb:bb9e0f6a-b882-4368-86d3-46288eb438df@ondemand.saucelabs.com:80/wd/hub"
)


# This is required for testing with Chrome.
#chrome_driver = './definitions/chromedriver_linux'
#chrome_driver = './definitions/chromedriver_mac'
#os.environ["webdriver.chrome.driver"] = chrome_driver
#driver = webdriver.Chrome(chrome_driver)
#driver = webdriver.Firefox()


# To quickly test the driver uncomment the following lines and run python
# test_settings.py

# driver.get("http://stackoverflow.com")
# driver.quit()
