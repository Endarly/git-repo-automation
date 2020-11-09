from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ContrapartePage:
    def __init__(self, driver):
        self.driver = driver

    _contrapartes = "//div[contains(text(),'CONTRAPARTE')]"
    _que_buscar = "//*[@id='search']"
    _lupa = "//*[@class='sc-AxiKw fDcFlR']"
    _contrap_selecc = "//div[contains(text(),'DEFAULT DOXTOR')]"
    _path = "counterpart/"
    _path_count ="1"
    _por_vencer = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='number porvencer']"
    _vencidos = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='number vencidos']"
    _pais = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='pais']"
    _num_doc = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='contracts'='1']"
    _ver_mas = "//*[@class='sc-fzplWN fTXodw']/child::div[1]"
    _todos_titulo ="//div[contains(text(),'Todos')]"
    _vigentes_titulo = "//div[contains(text(),'Vigentes')]"
    _por_vencer_titulo = "//div[contains(text(),'Por vencer')]"
    _vencidos_titulo = "//div[contains(text(),'Vencidos')]"
    _contraparte_titulo = "//div[contains(text(),'Contraparte')]"
    _busqueda_avanzada = "//*[@d='M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z']"
    _bus_por_num = "//*[contains(text(),'Buscar solo por número de documento')]"
    _bus_conatel = "//*[contains(text(),'Buscar solo en Conatel')]"
    _seleccionar_pais = "//*[@class='sc-fznJRM fntwKu']//*[@class='basic-single css-2b097c-container']"
    _tipo_documento = "//*[contains(text(),'Tipo de Documento')]"
    _contrato = "//*[@id='1']"
    _adenda = "//*[@id='2']"
    _carta_oferta = "//*[@id=3']"
    _convenio = "//*[@id='4']"
    _poder = "//*[@id='5']"
    _escritura = "//*[@id='6']"
    _regulacion = "//*[@id='7']"
    _nota = "//*[@id='8']"
    _resolucion = "//*[@id='9']"
    _plazo = "//*[contains(text(),'Plazo')]"
    _boton_aplicar = "//button[contains(text(),'Aplicar')]"
    _boton_cancelar = "//button[contains(text(),'Cancelar')]"
    _contraparte_buscar = "DEFAULT DOXTOR"
    _texto_busqueda_avanzada = "//div[contains(text(),'Búsqueda avanzada')]"

    def account_contraparte(self):
        contrapartes = self.driver.find_element(By.XPATH,self._contrapartes)
        contrapartes.click()

    def account_buscar(self):
        quebuscar = self.driver.find_element(By.XPATH,self._que_buscar)
        quebuscar.send_keys(Keys.TAB)
        quebuscar.send_keys(self._contraparte_buscar)
        lupa = self.driver.find_element(By.XPATH,self._lupa)
        lupa.click()

    def contraparte_seleccionada(self):
        contraparte= self.driver.find_element(By.XPATH,self._contrap_selecc)
        return contraparte.text

    def seleccionar_contraparte(self):
        contraparte= self.driver.find_element(By.XPATH,self._contraparte_buscar)
        contraparte.click()

    #def seleccionar_contraparte(self):
    #    contraparte= self.driver.find_element(By.XPATH,self._contrap_selecc)
    #    contraparte.click()
    #    time.sleep(3)

    def seleccionar_busqueda_avanzada(self):
        busqueda = self.driver.find_element(By.XPATH,self._busqueda_avanzada)
        busqueda.click()
        time.sleep(3)
        buscar_numero =self.driver.find_element(By.XPATH,self._bus_por_num)
        buscar_numero.click()
        aplicar = self.driver.find_element(By.XPATH,self._boton_aplicar)
        aplicar.click()
        #return te


#queda pendiemte la busqueda avanzad


    #def ordenar_por(self):
    #    ordenar_x_numero= self.__format__(By.XPATH,self.)


        #seleccionar = self.driver.find_element(By.XPATH, self._contrap_selecc)
        #seleccionar.send_keys(self._contraparte_buscar)

        #nombre_contraparte =self.driver.find_element(By.XPATH,self._contrap_selecc)
        #time.sleep(3)
        #return nombre_contraparte.text


    #def contraparte_seleccionada(self):
    #    contraparte_seleccionada= self.driver.find_element(By.XPATH, self._contrap_selecc)
    #    contraparte_seleccionada.click()

    #def ordenar_por(self):
     #   ordenar_numero = self.driver.find_element(By.XPATH, self._c)

