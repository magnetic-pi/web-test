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


class DragDropTest (unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.domain = definitions.exist_user_settings.sel_domain
        self.driver = definitions.test_settings.driver
        self.url = definitions.test_settings.baseUrl
        self.waitTime = definitions.test_settings.waitTime
        print self.email
        print self.password

    def test_drag_drop(self):
        print "Reorder site test is commencing."
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

        print "Selecting Store to edit."
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Jon's Site")))
        self.driver.find_element_by_link_text("Jon's Site").click()

        print "Make sure drag and drop elements exist before starting drag and drop."
        try:
            self.assertTrue(self.is_element_present(By.XPATH, "//li[2]/div[2]/div/div"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertTrue(self.is_element_present(By.XPATH, "//div[2]/div/h2"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        print "Elements exist. Get first item on lists location."
        hover_element1 = self.driver.find_element_by_xpath("//div[2]/div/h2")
        hover_action1 = ActionChains(self.driver)
        hover_action1.move_to_element(hover_element1).perform()
        time.sleep(4)

        print "Deleting the first item on the list."
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/div/ul/li/div/div[3]/div"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div[3]/div/div/span"))).click()

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
        print "The test has ended."
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
