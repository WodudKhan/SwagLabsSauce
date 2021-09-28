import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects import Locators
from tests.conftest import driver
from utilities.baseClass import BaseClass


class CheckoutPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    PRODUCT_PAGE_TITLE = (By.XPATH, "//span[contains(text(),'Products')]")
    CART_TITTLE = (By.XPATH, "//span[contains(text(),'Your Cart')]")
    CHECKOUT_HEADER_INFO = (By.XPATH, "//span[contains(text(),'Checkout: Your Information')]")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    CHECKOUT_OVERVIEW_HEADER = (By.XPATH, "//span[contains(text(),'Checkout: Overview')]")
    VERIFY_TOTAL = (By.CSS_SELECTOR, "div[class='summary_total_label']")
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    CHECKOUT_COMPLETE_HEADER = (By.XPATH, "//span[contains(text(),'Checkout: Complete!')]")
    THANK_YOU_TEXT_VALIDATION = (By.XPATH, "//h2[contains(text(),'THANK YOU FOR YOUR ORDER')]")

    def get_product_title(self):
        if self.get_element_text(self.PRODUCT_PAGE_TITLE):
            return self.get_element_text(self.PRODUCT_PAGE_TITLE)

    def get_header_cart_title(self):
        if self.get_element_text(self.CART_TITTLE):
            return self.get_element_text(self.CART_TITTLE)

    def get_checkOut_info_tittle(self):
        if self.get_element_text(self.CHECKOUT_HEADER_INFO):
            return self.get_element_text(self.CHECKOUT_HEADER_INFO)

    def get_checkOut_overview_tittle(self):
        if self.get_element_text(self.CHECKOUT_OVERVIEW_HEADER):
            return self.get_element_text(self.CHECKOUT_OVERVIEW_HEADER)

    def get_checkOut_complete_tittle(self):
        if self.get_element_text(self.CHECKOUT_COMPLETE_HEADER):
            return self.get_element_text(self.CHECKOUT_COMPLETE_HEADER)

    def clickCheckoutBtn(self):
        return self.driver.find_element(*CheckoutPage.CHECKOUT_BTN)

    def clickFinishBtn(self):
        return self.driver.find_element(*CheckoutPage.FINISH_BTN)

    def enterFirstName(self):
        return self.driver.find_element(*CheckoutPage.FIRST_NAME)

    def enterLastName(self):
        return self.driver.find_element(*CheckoutPage.LAST_NAME)

    def enterPostalCode(self):
        return self.driver.find_element(*CheckoutPage.POSTAL_CODE)

    def getContinueBtn(self):
        return self.driver.find_element(*CheckoutPage.CONTINUE_BTN)

    def enter_checkOut_Info(self, firstname, lastname, zipcode):
        self.do_send_keys(self.FIRST_NAME, firstname)
        self.do_send_keys(self.LAST_NAME, lastname)
        self.do_send_keys(self.POSTAL_CODE, zipcode)
        self.do_click(self.CONTINUE_BTN)

    def getTotal(self):
        if self.is_visible(self.VERIFY_TOTAL):
            return self.get_element_text(self.VERIFY_TOTAL)

    def thankyouOrderMessage(self):
        if self.is_visible(self.THANK_YOU_TEXT_VALIDATION):
            return self.get_element_text(self.THANK_YOU_TEXT_VALIDATION)
