from base.base_page import BasePage
import utilities.custom_logger as cl
import logging

class DoxtorLogin(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email = "//*[@id='username']"
    _password = "//*[@id='password']"
    _inicia_sesion = "//button[contains(text(),'INICIA SESIÓN')]"

    def enterEmail(self, email):
        self.sendKeys(email, self._email, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._inicia_sesion, locatorType="xpath")

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()