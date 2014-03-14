from selenium import webdriver
from time import gmtime, strftime, sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import definitions.exist_user_settings
import definitions.test_settings
import unittest
import re


class FailLoginTest(unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.domain = definitions.exist_user_settings.sel_domain
        self.driver = definitions.test_settings.driver
        self.url = definitions.test_settings.baseUrl
        self.waitTime = definitions.test_settings.waitTime
        print self.driver
        print self.url
        print self.username

    def test_fail_login(self):
        print "Starting Login and Logout Test"
        wait = WebDriverWait(self.driver, self.waitTime)

        self.driver.get(self.url)
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-username'))).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, 'weebly-password'))).click()
        Username = self.driver.find_element_by_id('weebly-username')
        Username.send_keys(self.email)
        Password = self.driver.find_element_by_id('weebly-password')
        Password.send_keys("wrong")
        self.driver.find_element_by_xpath("//input[@value='Log in']").click()
        for i in range(60):
            try:
                if "Wrong username or password" == self.driver.find_element_by_css_selector("div.popover-content").text:
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        try:
            self.assertEqual("Wrong username or password", self.driver.find_element_by_css_selector(
                "div.popover-content").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

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
        print "The test has ended"
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
