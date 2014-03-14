import unittest, time
from selenium import webdriver
from time import sleep
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import definitions.new_user_settings
import definitions.sauce_settings


class RegisterTest(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '27'
        desired_capabilities['platform'] = 'Linux'
        desired_capabilities['name'] = 'Testing Weebly Registration.'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://jcostellowb:bb9e0f6a-b882-4368-86d3-46288eb438df@ondemand.saucelabs.com:80/wd/hub"
        )
	self.waitTime = definitions.sauce_settings.waitTime
        self.username = definitions.new_user_settings.username
        self.email = definitions.new_user_settings.email
        self.password = definitions.new_user_settings.password
        self.domain = definitions.new_user_settings.sel_domain
        self.url = definitions.sauce_settings.baseUrl
        #print self.driver
        print self.url
        #print self.username

    def test_registration(self):
        print "Registration test is commencing"
        wait = WebDriverWait(self.driver, self.waitTime)
        self.driver.get(self.url)
        wait.until(EC.element_to_be_clickable((By.ID, 'weebly-name'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'weebly-email'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.ID, 'weebly-new-password'))).click()
        Username = self.driver.find_element_by_id('weebly-name')
        Username.send_keys(self.username)
        print "Entered a username of %s on the landing page" % self.username
        Useremail = self.driver.find_element_by_id('weebly-email')
        Useremail.send_keys(self.email)

        print "Entered email as %s on the landing page." % self.email
        Password = self.driver.find_element_by_id('weebly-new-password')
        Password.send_keys(self.password)

        print "Entered a password of %s on the landing page." % self.password
        submitReg = self.driver.find_element_by_id('signup-button-default')
        submitReg.click()

        print "A/B Testing site type if it appears."
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[2]/div/div/div").click()
        except:
            print "No A/B test appeared."

        time.sleep(2)
        print "Choosing the first theme on the page."
        wait.until(EC.presence_of_element_located((By.ID, 'choose-theme')))
        self.driver.find_element_by_xpath(
            "//ul[@id='w-theme-list']/li[2]/div/img")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//ul[@id="w-theme-list"]/li/div/div/div/button'))).click()
        print "Choosing a weebly domain name."
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='chooseDomainDiv']/div[2]/a/span")
        ))
        self.driver.find_element_by_xpath(
            "//div[@id='domainSubdomain']/div/input").click()
        DomainName = self.driver.find_element_by_id('weeblyDomain')
        DomainName.send_keys(self.domain)
        self.driver.find_element_by_xpath(
            "//div[@id='chooseDomainDiv']/div[2]/a/span").click()
        wait.until(EC.element_to_be_clickable(
            (By.ID, 'planning-info-continue'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@id='more-drop-button']/a/span"))).click()
        print "Closing the editor"
        wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Exit Editor"))).click()
        print "Logging out of weebly."
        wait.until(
            EC.element_to_be_clickable((By.ID, 'site-types-never'))).click()
        self.driver.find_element_by_xpath(
            "//div[@id='categorize-sites']/div[2]/div[3]/a[2]/span").click()
        print "Logged In"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
                   ).click()

    def tearDown(self):
        print "The test has ended"
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
