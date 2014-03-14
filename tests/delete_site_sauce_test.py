from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.action_chains import ActionChains
import definitions.exist_user_settings
import definitions.sauce_settings
import unittest
import time


class DeleteSiteTest(unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.domain = definitions.exist_user_settings.sel_domain
        self.driver = definitions.sauce_settings.driver
        self.url = definitions.sauce_settings.baseUrl
        self.waitTime = definitions.sauce_settings.waitTime
        print self.email
        print self.password

    def test_edit_site(self):
        print "Delete site test is commencing."
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
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@id='weebly-login']/p[4]/input"))).click()

        print "Selecting Site to delete."
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[3]/span"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div/div/div/ul/li[4]/a/span"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div/div[2]/div[3]/a"))).click()

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
        print "The test has ended."
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
