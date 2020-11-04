from pages.home_phptravels import HomePhpTravels as HPT
from pages.login_phptravels import LoginPhpTravels as LPT
from pages.account_page import AccountPage as AP
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory as wd

@pytest.mark.usefixtures()
class LoginTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    email = "user@phptravels.com"
    password = "demouser"
    driver = wd("chrome")
    _url = "https://www.phptravels.net/"

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.driver =self.driver.getWebDriverInstance(self._url)
        self.hp = HPT(self.driver)
        self.lp = LPT(self.driver)
        self.ap = AP(self.driver)

    #@pytest.mark.run(order=1)
    def test_validLogin(self):
        accountName = "Hi, Demo User"
        self.log.info("*#" * 20)
        self.log.info("test_validLogin started")
        self.log.info("*#" * 20)
        self.hp.login()
        self.lp.login(self.email, self.password)
        assert (self.ap.account_name() == accountName)
        assert (self.driver.current_url == self._url + self.ap._path)

        self.ap.newsletter_action()
        assert ("active" in self.ap.subscribe_class())

        self.ap.logout_action()
        assert (self.driver.current_url == self._url + self.lp._path)