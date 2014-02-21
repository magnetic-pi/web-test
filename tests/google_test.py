from selenium import webdriver
from time import sleep
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import definitions.user_settings
import definitions.test_settings
import unittest


class RegisterTest (unittest.TestCase):
    def setUp(self):
        self.username = definitions.user_settings.username
        self.email    = definitions.user_settings.email
        self.password = definitions.user_settings.password
        self.domain   = definitions.user_settings.sel_domain
        self.driver   = definitions.test_settings.driver
        self.url      = "www.google.com"
        self.waitTime = definitions.test_settings.waitTime
        #print self.driver
        #print self.url
        #print self.username

    def test_Register(self):
        print "Registration test is commencing"
        #print "register"
        wait = WebDriverWait(self.driver, self.waitTime)
        self.driver.get(self.url)
        wait.until(EC.element_to_be_clickable((By.ID, 'weebly-name'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'weebly-email'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'weebly-new-password'))).click()
        Username = self.driver.find_element_by_id('weebly-name')
        Username.send_keys(self.username)
        print self.username
        Useremail = self.driver.find_element_by_id('weebly-email')
        Useremail.send_keys(self.email)
        print self.email
        Password = self.driver.find_element_by_id('weebly-new-password')
        Password.send_keys(self.password)
        print self.password
        submitReg = self.driver.find_element_by_id('signup-button-default')
        submitReg.click()
        wait.until(EC.presence_of_element_located((By.ID, 'choose-theme')))
        theme = self.driver.find_element_by_xpath("//ul[@id='w-theme-list']/li[2]/div/img")
	    #print theme
        hover = ActionChains(self.driver).move_to_element(theme).perform()
	    #print hover
        wait.until(EC.element_to_be_clickable((By.XPATH, '//li[2]/div/div/div/button'))).click()
        #sel_ent = self.driver.find_element_by_xpath("//ul[@id='w-theme-list']/li[2]/div/div/div/button")
        #sel_ent.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[90]/div/div/div/div[2]/div/div/div[2]/form/div/div/input'))).click() 
        DomainName = self.driver.find_element_by_id('weeblyDomain') 
        DomainName.send_keys(self.domain)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@onclick='domainChoiceContinue(); return done();']"))).click() 
        wait.until(EC.element_to_be_clickable((By.ID, 'planning-info-continue'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='more-drop-button']/a/span"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Exit Editor"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='weebly-bluebox-container']/div"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

    def tearDown(self):
        print "The test has ended"
        self.driver.quit()
