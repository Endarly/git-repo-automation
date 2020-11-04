from selenium.webdriver.common.by import By


class HomePhpTravels:
    def __init__(self, driver):
        self.driver = driver

    _account = "//*[@class ='dropdown dropdown-login dropdown-tab']"
    _login_link = "//a[@ class ='dropdown-item active tr']"

    def login(self):
        account = self.driver.find_element(By.XPATH,self._account)
        account.click()
        login_link = self.driver.find_element(By.XPATH,self._login_link)
        login_link.click()