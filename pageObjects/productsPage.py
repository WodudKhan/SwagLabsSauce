from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects import Locators
from tests.conftest import driver
from utilities.baseClass import BaseClass



class ProductPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    PAGE_HEADER = (By.XPATH, "//span[contains(text(),'Products')]")
    BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.CSS_SELECTOR, "button[id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    SHOPPINGCARTLINK = (By.CLASS_NAME, "shopping_cart_badge")



    def get_header_value(self):
        if self.get_element_text(self.PAGE_HEADER):
            return self.get_element_text(self.PAGE_HEADER)

    def addBackpack(self):
        return self.driver.find_element(*ProductPage.BACKPACK)

    def addTshirt(self):
        return self.driver.find_element(*ProductPage.TSHIRT)

    def clickShoppingCart(self):
        return self.driver.find_element(*ProductPage.SHOPPINGCARTLINK)

    def add_item_to_cart(self):
        self.do_click(self.BACKPACK)
        self.do_click(self.TSHIRT)
        self.do_click(self.SHOPPINGCARTLINK)


    # # Below function use to get element exist - I am not using this in this app at the moment signup link dont exist
    # def is_signup_link_exist(self):
    #     return self.is_visible(self.SIGNUP_LINK)



