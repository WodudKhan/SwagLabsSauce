import time
import unittest
from unittest import TestCase

import pytest
import self

from pageObjects.loginPage import LoginPage
from testData.loginPageData import LoginPageData
from utilities.baseClass import BaseClass


class TestLoginPage(BaseClass):

    @pytest.fixture(autouse=True)
    def objectSetup(self, setup):
        self.loginPage = LoginPage(self.driver)
        self.log = self.getLogger()

    def test_login_page_title(self):
        title = self.loginPage.get_title(LoginPageData.LOGIN_PAGE_TITLE)
        assert title == LoginPageData.LOGIN_PAGE_TITLE
        self.log.info("Page tittle is " + title)

    def test_login_text_exist(self):
        textPresence = self.loginPage.verifyText()
        assert textPresence == LoginPageData.LOGIN_PAGE_CREDENTIAL
        self.log.info("Text 'password for all users' displayed")

    def test_loginformGroup(self, getData):
        self.log.info("User name is " + getData["Username"])
        self.loginPage.login(LoginPageData.USER_NAME, LoginPageData.PASSWORD)
        self.log.info("Username entered into the usernameInput textField")
        self.log.info("Password entered into the passwordInput textField")
        self.log.info("User clicked on signIn btn")
        self.log.info("User successfully logged in to the app")

    @pytest.fixture(params=LoginPageData.TEST_LOGIN_PAGE_DATA)
    def getData(self, request):
        return request.param
