import pytest
import sys

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.loginPage import LoginPage
from pageObjects.productsPage import ProductPage
from testData.loginPageData import LoginPageData
from utilities.baseClass import BaseClass


class TestCheckoutPage(BaseClass):

    # @pytest.mark.smoke  # This is my custom marker
    @pytest.fixture(autouse=True)
    def objectSetup(self, setup):
        self.loginPage = LoginPage(self.driver)
        self.productPage = ProductPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)
        self.log = self.getLogger()

    # @pytest.mark.skipif(sys.version_info < (3, 7), reason="Python version not supported")
    def test_checkout_cart_header(self):
        self.loginPage.login(LoginPageData.USER_NAME, LoginPageData.PASSWORD)
        self.productPage.add_item_to_cart()

        header = self.checkoutPage.get_header_cart_title()
        assert header == LoginPageData.CART_HEADER_TITLE
        self.log.info("Cart header tittle is " + header)
        self.checkoutPage.clickCheckoutBtn().click()
        self.log.info("UI checkout btn clicked")

    # @pytest.mark.xfail  # this will show you when the test fail
    def test_checkout_info_header(self):
        header = self.checkoutPage.get_checkOut_info_tittle()
        # print(header)
        assert header == LoginPageData.CHECKOUT_INFO_TITLE
        self.log.info("Checkout info header tittle is " + header)

    # @pytest.mark.parametrize
    def test_info_formGroup(self):
        self.checkoutPage.enter_checkOut_Info(LoginPageData.ENTER_FIRSTNAME, LoginPageData.ENTER_LASTNAME,
                                              LoginPageData.ENTER_ZIP_CODE)
        self.log.info("User entered checkout information")

    def test_checkOut_overview(self):
        header = self.checkoutPage.get_checkOut_overview_tittle()
        # print(header)
        assert header == LoginPageData.CHECKOUT_OVERVIEW_TITLE
        self.log.info("Checkout header tittle is " + header)

    def test_checkOut_total(self):
        total = self.checkoutPage.getTotal()
        # print(total)
        self.log.info("Checkout sum total is " + total)
        self.checkoutPage.clickFinishBtn().click()
        self.log.info("UI Finish btn clicked")

    def test_checkOut_complete_header(self):
        header = self.checkoutPage.get_checkOut_complete_tittle()
        # print(header)
        assert header == LoginPageData.CHECKOUT_COMPLETE_TITLE
        self.log.info("Checkout header tittle is " + header)

        assertText = self.checkoutPage.thankyouOrderMessage()
        # print(textPresence)
        assert assertText == LoginPageData.THANK_YOU_TEXT
        self.log.info("UI Thank you message displayed as " + assertText)

    @pytest.fixture(params=LoginPageData.TEST_LOGIN_PAGE_DATA)
    def getData(self, request):
        return request.param
