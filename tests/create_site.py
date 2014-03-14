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


class CreateSiteTest (unittest.TestCase):

    def setUp(self):
        self.username = definitions.exist_user_settings.username
        self.email = definitions.exist_user_settings.email
        self.password = definitions.exist_user_settings.password
        self.domain = definitions.exist_user_settings.sel_domain
        self.driver = definitions.test_settings.driver
        self.url = definitions.test_settings.baseUrl
        self.waitTime = definitions.test_settings.waitTime
        action_chains = ActionChains(self.driver)
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
        # time.sleep(2)

        print "Clicking create site button."
        # time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.ID, 'create-site-button'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'create-site-button'))).click()
        print "Clicked create site button."
        time.sleep(2)

        print "Selecting site theme of: First Theme"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt=\"Light\"]")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
        hover_element = self.driver.find_element_by_xpath("//ul[@id='w-theme-list']/li/div/img")
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(hover_element).perform()
        theme = self.driver.find_element_by_xpath(
            "//ul[@id='w-theme-list']/li[2]/div/img")
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
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
        self.driver.find_element_by_id("wsite-title").send_keys("Jon's Site")
        time.sleep(1)
        # self.driver.find_element_by_id("main").click()

        print "Finding title from toolbar starting drag and drop"
        self.driver.find_element_by_css_selector("div.title-box").click()
        title = self.driver.find_element_by_xpath(
            "//ul[@id='anonymous_element_7']/li/div[2]")
        self.driver.find_element_by_id("main").click()
        title_target = self.driver.find_element_by_id("empty-message-inner")
        self.driver.find_element_by_id("main").click()
        drag_title = ActionChains(self.driver)
        drag_title.drag_and_drop(title, title_target).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//h2").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//h2").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//h2").send_keys("Drag and drop title text change.")
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[2]/div[2]").click()
        time.sleep(1)

        print "Drag and drop title sould now be complete."

        time.sleep(2)

        print "Finding text from toolbar and starting drag and drop."
        try:
            self.assertTrue(self.is_element_present(By.ID, "secondlist"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        wait.until(EC.presence_of_element_located((By.ID, "secondlist")))
        self.driver.find_element_by_xpath("//li[2]/div[2]").click()
        text = self.driver.find_element_by_xpath("//li[2]/div[2]")
        text_target = self.driver.find_element_by_id("secondlistParent")
        drag_text = ActionChains(self.driver)
        drag_text.drag_and_drop(text, text_target).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[2]/div[2]/div/div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[2]/div[2]/div/div").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[2]/div[2]/div/div").send_keys("Drag and drop text area testing text input.")
        time.sleep(3)
        self.driver.find_element_by_xpath("//li[2]/div[2]").click()
        print "Drag and drop sould now be complete."
        # wait.until(EC.element_to_be_clickable(
        #    (By.XPATH, "//li[@id='more-drop-button']/a/span"))).click()
        # wait.until(EC.element_to_be_clickable(
        #    (By.LINK_TEXT, "Exit Editor"))).click()
        # wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        #           ).click()

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
