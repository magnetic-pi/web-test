from selenium import webdriver
from time import sleep
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import definitions.exist_user_settings
import definitions.test_settings
import unittest


class ChangePassword(unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.reset_pass = definitions.exist_user_settings.reset_pw
        self.domain = definitions.exist_user_settings.sel_domain
        self.driver = definitions.test_settings.driver
        self.url = definitions.test_settings.baseUrl
        self.waitTime = definitions.test_settings.waitTime
        print self.url
        print self.username

    def test_pw_change(self):
        print "Changing Password"
        # print "register"
        wait = WebDriverWait(self.driver, self.waitTime)
        self.driver.get(self.url)
        print "Logging in."
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-username'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-password'))).click()
        Username = self.driver.find_element_by_id('weebly-username')
        Username.send_keys(self.email)
        print self.email
        Password = self.driver.find_element_by_id('weebly-password')
        Password.send_keys(self.password)
        print self.password
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//form[@id='weebly-login']/p[4]/input"))).click()
            print "Logged In"
        except:
            print "The elements do not exist"

        print "Clicking account link."
        self.driver.find_element_by_xpath(
            "//a[contains(text(),'Account')]").click()

        print "Changing password."
        self.driver.find_element_by_link_text("change").click()
        self.driver.find_element_by_id("new-password").clear()
        self.driver.find_element_by_id(
            "new-password").send_keys(self.reset_pass)
        self.driver.find_element_by_id("repeat-password").clear()
        self.driver.find_element_by_id(
            "repeat-password").send_keys(self.reset_pass)
        self.driver.find_element_by_xpath(
            "//div[@id='account-change-password']/div[2]/div[3]/a/span").click()
        self.driver.find_element_by_link_text("Logout").click()
        self.driver.find_element_by_id("logInButton").click()

        print "Testing that the user can log in with the new password."
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-username'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-password'))).click()
        Username = self.driver.find_element_by_id('weebly-username')
        Username.send_keys(self.email)
        Password = self.driver.find_element_by_id('weebly-password')
        Password.send_keys(self.reset_pass)
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//form[@id='weebly-login']/p[4]/input"))).click()
            print "Logged In"
        except:
            print "The elements do not exist"
        self.driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        print "The test has ended"
        self.driver.quit()
