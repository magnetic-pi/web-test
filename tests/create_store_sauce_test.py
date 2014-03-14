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


class CreateStoreTest(unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.domain = definitions.exist_user_settings.store_domain
        self.driver = definitions.sauce_settings.driver
        self.url = definitions.sauce_settings.baseUrl
        self.waitTime = definitions.sauce_settings.waitTime
        print self.email
        print self.password

    def test_create_store(self):
        print "Create store test is commencing."
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
        time.sleep(2)

        print "A/B Testing site type if it appears."
        try:
            self.driver.find_element_by_xpath("//div[3]").click()
        except:
            print "No A/B test appeared."
        time.sleep(2)

        print "Selecting site theme of: First Theme"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt=\"Lucent\"]")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
        hover_element = self.driver.find_element_by_css_selector("img[alt=\"Lucent\"]")
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(hover_element).perform()
        theme = self.driver.find_element_by_xpath(
            "//ul[@id='w-theme-list']/li[2]/div/img")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[@id='w-theme-list']/li[2]/div/div/div/button"))).click()
        print "Theme Selected"

        print "Selecting Domain"
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='chooseDomainDiv']/div[2]/a/span")
        ))
        self.driver.find_element_by_xpath(
            "//div[@id='domainSubdomain']/div/input").click()
        DomainName = self.driver.find_element_by_id('weeblyDomain')
        DomainName.send_keys(self.domain)
        self.driver.find_element_by_xpath(
            "//div[@id='chooseDomainDiv']/div[2]/a/span").click()

        print "Editing the existing title."
        self.driver.find_element_by_id("wsite-title").click()
        time.sleep(1)
        self.driver.find_element_by_id("wsite-title").clear()
        time.sleep(1)
        self.driver.find_element_by_id("wsite-title").send_keys("Jon's Store")
        time.sleep(1)

        print "Adding an item to the store."
        self.driver.find_element_by_xpath("//div[2]/span[2]").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, 'editor_commerce_product_name'))).click()
        self.driver.find_element_by_id("editor_commerce_product_name").clear()
        self.driver.find_element_by_id("editor_commerce_product_name").send_keys("test product")
        self.driver.find_element_by_id("editor_commerce_product_short_description").clear()
        self.driver.find_element_by_id("editor_commerce_product_short_description").send_keys("this is a test short description")
        self.driver.find_element_by_id("editor_commerce_product_price").clear()
        self.driver.find_element_by_id("editor_commerce_product_price").send_keys("10")
        self.driver.find_element_by_id("editor_commerce_product_sale_price").clear()
        self.driver.find_element_by_id("editor_commerce_product_sale_price").send_keys("10")
        self.driver.find_element_by_xpath("//div[@id='commerce_editor']/div/div/div/div/div/div[9]/div/button[2]").click()

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

if __name__ == '__main__':
    unittest.main()
