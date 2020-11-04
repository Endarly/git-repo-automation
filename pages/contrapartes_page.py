from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ContrapartePage:
    def __init__(self, driver):
        self.driver = driver

    _contrapartes = "//*[@class='sc-fzqLLg hjnSEH']//a[@href='/']"
    _que_buscar = "//*[@id='search']"
    _lupa = "//*[@class='sc-AxiKw fDcFlR']"
    _contraparte_seleccionada = "//*[@name='DEFAULT DOXTOR']"

    def account_contraparte(self):
        contrapartes = self.driver.find_element(By.XPATH,self._contrapartes)
        contrapartes.click()

    def account_buscar(self):
        quebuscar = self.driver.find_element(By.XPATH,self._que_buscar)
        quebuscar.send_keys(Keys.TAB)
        quebuscar.send_keys("DEFAULT DOXTOR")
        lupa = self.driver.find_element(By.XPATH,self._lupa)
        lupa.click()
        contraparte_seleccionada= self.driver.find_element(By.XPATH, self._contraparte_seleccionada)
        contraparte_seleccionada.click()