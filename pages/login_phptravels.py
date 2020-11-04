from base.base_page import BasePage
import utilities.custom_logger as cl
import logging


class LoginPhpTravels(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _path = "login"
    _email = "username"
    _password = "password"
    _button_login = "//button[contains(text(),'Login')]"
    _remember_me = "//*[contains(text(),'Remember Me')]"
    _login = "//h3[contains(text(), 'Login')]"

    def enterEmail(self, email):
        self.sendKeys(email, self._email, locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self._password, locatorType="name")

    def clickLoginButton(self):
        self.elementClick(self._button_login, locatorType="xpath")

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()