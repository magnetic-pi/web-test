from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import definitions.exist_user_settings
import definitions.test_settings
import unittest, time


class CreateSiteTest (unittest.TestCase):

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

    def test_create_site(self):
        print "Create site test is commencing."
        # print "register"
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
	print "Clicking create site button."
	wait.until(EC.element_to_be_clickable((By.ID, 'create-site-button'))).click()
	print "Clicked create site button."
	wait.until(EC.presence_of_element_located((By.ID, 'choose-theme')))
	print "Selecting site theme of: First Theme"
        wait.until(EC.presence_of_element_located((By.ID, 'choose-theme')))
        theme = self.driver.find_element_by_xpath(
            "//ul[@id='w-theme-list']/li[2]/div/img")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//ul[@id="w-theme-list"]/li/div/div/div/button'))).click()
        ##hover = ActionChains(self.driver).move_to_element(theme).perform()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='chooseDomainDiv']/div[2]/a/span")
        ))
        self.driver.find_element_by_xpath(
            "//div[@id='domainSubdomain']/div/input").click()
        DomainName = self.driver.find_element_by_id('weeblyDomain')
        DomainName.send_keys(self.domain)
        self.driver.find_element_by_xpath(
            "//div[@id='chooseDomainDiv']/div[2]/a/span").click()
        
        #wait.until(EC.element_to_be_clickable(
        #    (By.XPATH, "//li[@id='more-drop-button']/a/span"))).click()
        #wait.until(EC.element_to_be_clickable(
        #    (By.LINK_TEXT, "Exit Editor"))).click()
        #wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        #           ).click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def tearDown(self):
        print "The test has ended"
        self.driver.quit()
