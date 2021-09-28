import self
from selenium.webdriver.common.by import By
from utilities.baseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # Locators
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    TEXT_EXIST = (By.CSS_SELECTOR, "div[class='login_password'] h4")

    def getUser(self):
        return self.driver.find_element(*LoginPage.USER_NAME)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.PASSWORD)

    def click_login_btn(self):
        return self.driver.find_element(*LoginPage.LOGIN_BTN)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def verifyText(self):
        if self.is_visible(self.TEXT_EXIST):
            return self.get_element_text(self.TEXT_EXIST)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def login(self, username, password):
        self.clearFields()
        self.do_send_keys(self.USER_NAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)

    def clearFields(self):
        userField = self.driver.find_element(*LoginPage.USER_NAME)
        userField.clear()
        passwordField = self.driver.find_element(*LoginPage.PASSWORD)
        passwordField.clear()
        return
