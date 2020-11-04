from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DoxtorLogin:
    def __init__(self, driver):
        self.driver = driver

    _legajo = "//*[@id='username']"
    _password = "//*[@id='password']"
    _inicia_sesion = "//button[contains(text(),'INICIA SESIÓN')]"

    def login(self):
        legajo = self.driver.find_element(By.XPATH, self._legajo)
        legajo.send_keys(Keys.TAB)
        legajo.send_keys("EXB30522")

        password = self.driver.find_element(By.XPATH, self._password)
        legajo.send_keys(Keys.TAB)
        password.send_keys("Viernes43*")

        inicia_sesion= self.driver.find_element(By.XPATH,self._inicia_sesion)
        inicia_sesion.click()