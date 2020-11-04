from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    _user_account = "//input[contains(text(),'')]"
    #_contrapartes = "//*[@class='sc-fzqLLg hjnSEH']//a[@href='/']"
    _documentos = "//*[@class='sc-fzqLLg hjnSEH']//a[@href='/all_documents']"
    _colaprocesos = "//*[@class='sc-fzqLLg hjnSEH']//a[@href='/process_stack']"
    _reportes ="//*[@class='sc-fzqLLg hjnSEH']//a[@href='/reports']"
    _ajustes = "//*[@class='sc-fzqLLg hjnSEH']//a[@href='/settings']"


    def account_user(self):
        user_account= self.driver.find_element(By.XPATH,self._user_account)
        return user_account.text

    #def account_contraparte(self):
    #    contrapartes = self.driver.find_element(By.XPATH,self._contrapartes)
    #    contrapartes.click()

    def account_documentos(self):
        documentos = self.driver.find_element(By.XPATH,self._documentos)
        documentos.click()

    def account_colaprocesos(self):
        colaprocesos = self.driver.find_element(By.XPATH,self._colaprocesos)
        colaprocesos.click()

    def account_reportes(self):
        reportes = self.driver.find_element(By.XPATH,self._reportes)
        reportes.click()

    def account_ajustes(self):
        ajustes = self.driver.find_element(By.XPATH,self._ajustes)
        ajustes.click()

