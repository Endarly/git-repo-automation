from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DocumentosPage:
    def __init__(self, driver):
        self.driver = driver

    _documentos = "//div[contains(text(),'DOCUMENTOS')]"
    _que_buscar = "//*[@id='search']"
    _lupa = "//*[@class='sc-AxiKw fDcFlR']"
    _documento_seleccionado = "//*[@id='81fcb830-147e-11eb-bf36-a59d44d12327']"
    _path = "all_documents"
    _path_doc = "document/81fcb830-147e-11eb-bf36-a59d44d12327"
    _ver = "//*[@href='/document/81fcb830-147e-11eb-bf36-a59d44d12327']"

    def account_documento(self):
        contrapartes = self.driver.find_element(By.XPATH,self._documentos)
        contrapartes.click()

    def account_buscar(self):
        quebuscar = self.driver.find_element(By.XPATH,self._que_buscar)
        quebuscar.send_keys(Keys.TAB)
        quebuscar.send_keys("DEFAULT DOXTOR")

        lupa = self.driver.find_element(By.XPATH,self._lupa)
        lupa.click()

        contraparte_seleccionada= self.driver.find_element(By.XPATH, self._documento_seleccionado)
        contraparte_seleccionada.click()

        visualizar_documento = self.driver.find_element(By.XPATH, self._ver)
        visualizar_documento.click()