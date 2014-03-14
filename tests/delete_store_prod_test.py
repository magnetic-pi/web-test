from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.action_chains import ActionChains
import definitions.exist_user_settings
import definitions.test_settings
import unittest
import time


class DelStoreItemTest (unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.domain = definitions.exist_user_settings.store_domain
        self.driver = definitions.test_settings.driver
        self.url = definitions.test_settings.baseUrl
        self.waitTime = definitions.test_settings.waitTime
        print self.email
        print self.password

    def test_del_store_item(self):
        print "Create site test is commencing."
        wait = WebDriverWait(self.driver, self.waitTime)
        self.driver.get(self.url)
        print "Starting logging in."
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-username'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-password'))).click()
        Username = self.driver.find_element_by_id('weebly-username')
        Username.send_keys(self.email)
        Password = self.driver.find_element_by_id('weebly-password')
        Password.send_keys(self.password)
        print "Login successful."
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//form[@id='weebly-login']/p[4]/input"))).click()
        except:
            print "The elements do not exist"

        print "Selecting Site to edit."
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Jon's Store")))
        self.driver.find_element_by_link_text("Jon's Store").click()

        print "Deleting store item."
        self.driver.find_element_by_xpath("//div/a/div[2]").click()
        wait.until(EC.presence_of_element_located((By.ID, "commerce_editor_editproductinstore"))).click()
        self.driver.find_element_by_xpath("//div[9]/button").click()
        time.sleep(2)
        alert = self.driver.switch_to_alert()
        alert.accept()
        #self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to delete this item[\s\S]$")
        time.sleep(2)
        self.driver.find_element_by_css_selector("div.store-nav-list-view > a.close-x").click()

        print "Exit the editor."
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@id='more-drop-button']/a/span"))).click()
        wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Exit Editor"))).click()
        print "Exited the editor"

        print "Log out"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
                   ).click()
        print "Logged out!"

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def tearDown(self):
        print "The test has ended"
        self.driver.quit()
