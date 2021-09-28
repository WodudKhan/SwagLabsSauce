import time

import pytest

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.loginPage import LoginPage
from testData.loginPageData import LoginPageData
from utilities.baseClass import BaseClass
from pageObjects.productsPage import ProductPage


class TestProductPage(BaseClass):

    @pytest.fixture(autouse=True)
    def objectSetup(self, setup):
        self.loginPage = LoginPage(self.driver)
        self.productPage = ProductPage(self.driver)
        self.productPage = ProductPage(self.driver)
        self.log = self.getLogger()

    def test_product_page_title(self, getData):
        self.loginPage.login(LoginPageData.USER_NAME, LoginPageData.PASSWORD)

        title = self.loginPage.get_title(LoginPageData.PRODUCT_PAGE_TITLE)
        # print(title)
        assert title == LoginPageData.PRODUCT_PAGE_TITLE
        self.log.info("Page tittle is " + title)

    def test_product_header_title(self):
        header = self.productPage.get_header_value()
        # print(header)
        assert header == LoginPageData.PRODUCT_HEADER_TITLE
        self.log.info("Header page tittle is " + header)

    def test_add_to_cart(self):
        self.productPage.add_item_to_cart()
        self.log.info("Items added to the shopping cart")

    @pytest.fixture(params=LoginPageData.TEST_LOGIN_PAGE_DATA)
    def getData(self, request):
        return request.param
