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
import time
import re


class ChangeEmail(unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.reset_email = definitions.exist_user_settings.reset_email
        self.domain = definitions.exist_user_settings.sel_domain
        self.driver = definitions.test_settings.driver
        self.url = definitions.test_settings.baseUrl
        self.waitTime = definitions.test_settings.waitTime
        print self.url

    def testChangeEmail(self):
        print "Start Changing Email Test"
        wait = WebDriverWait(self.driver, self.waitTime)
        self.driver.get(self.url)

        print "Logging In"
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
        except:
            print "The elements do not exist"

        print "Looking for the account link."
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Account')]"))).click()

        print "Changing email address."
        try:
            self.assertEqual(
                self.email, self.driver.find_element_by_id("current-email").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.driver.find_element_by_xpath(
            "(//a[contains(text(),'change')])[2]").click()
        self.driver.find_element_by_id("new-email").clear()
        self.driver.find_element_by_id("new-email").send_keys(self.reset_email)
        self.driver.find_element_by_xpath(
            "//div[@id='account-change-email']/div[2]/div[2]/a/span").click()
        try:
            self.assertTrue(self.is_element_present(By.ID, "current-email"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if self.reset_email == self.driver.find_element_by_id("current-email").text:
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        try:
            self.assertEqual(
                self.reset_email, self.driver.find_element_by_id("current-email").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.driver.find_element_by_link_text("Logout").click()
        self.driver.find_element_by_id("logInButton").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-username'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-password'))).click()
        Username = self.driver.find_element_by_id('weebly-username')
        Username.send_keys(self.reset_email)
        Password = self.driver.find_element_by_id('weebly-password')
        Password.send_keys(self.password)
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//form[@id='weebly-login']/p[4]/input"))).click()
            print "Logged In"
        except:
            print "The elements do not exist"
        self.driver.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def tearDown(self):
        print "The test has ended"
        self.driver.quit()
