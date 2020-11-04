from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ClaroLogin():
    title = "Inicia sesión"
    wait_time_out = 5
    driver = webdriver

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        email_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(@placeholder,'Ingresá tu correo electrónico')]")))
        email_field.send_keys("facebook")
        # email_field= driver.find_element_by_xpath("//*[contains(@placeholder,'Ingresá tu correo electrónico')]")
        pass_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.NAME, "pass")))
        pass_field.send_keys("1234")
        inicia_sesion = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'INICIA SESIÓN')]")))
        inicia_sesion.click()

        error_login = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//label[contains(text( ),'Debe contener entre 6 y 10 caracteres. Al menos un')]")))
        if error_login:
            print("mensaje de error login correcto")
        else:
            print("Error no aparece el mensaje de error")