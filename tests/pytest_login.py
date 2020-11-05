from pages.login_page import DoxtorLogin as LD
from pages.account_page import AccountPage as AP
from pages.contrapartes_page import ContrapartePage as CP
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory as wd

@pytest.mark.usefixtures()
class LoginTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    email = "EXB30522"
    password = "Viernes43*"
    driver = wd("chrome")
    _url = "http://10.92.114.78:3002/"

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.driver =self.driver.getWebDriverInstance(self._url)
        #self.hp = HPT(self.driver)
        self.ld = LD(self.driver)
        self.ap = AP(self.driver)

    #@pytest.mark.run(order=1)
    def test_validLogin(self):
        #accountName = "Qué desea buscar"
        self.log.info("*#" * 20)
        self.log.info("test_validLogin started")
        self.log.info("*#" * 20)
        #self.hp.login()
        self.ld.login(self.email, self.password)
        #assert (self.ap.account_user() == accountName)
        assert (self.driver.current_url == self._url)

        #self.ap.account_contraparte()
        #assert ("")

        self.ap.account_documentos()
        assert (self.driver.current_url == self._url + self.ap._path)
        #assert ("all_documents" in self.ap.account_documentos())

        #self.ap.newsletter_action()
        #assert ("active" in self.ap.subscribe_class())

        #self.ap.logout_action()
        #assert (self.driver.current_url == self._url + self.lp._path)