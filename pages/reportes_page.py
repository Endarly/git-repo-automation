from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ReportePage:
    def __init__(self, driver):
        self.driver = driver

    _reportes ="//div[contains(text(),'REPORTES')]"
    _path = "reports"
    _reporte_titulo = "//div[contains(text(), 'Reportes')]"


    def account_reporte(self):
        reportes = self.driver.find_element(By.XPATH,self._reportes)
        reportes.click()

    def reporte_titulo(self):
        titulo=self.driver.find_element(By.XPATH,self._reporte_titulo)
        return titulo.text