from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage
import utilities.custom_logger as cl
import logging
import time

class ContrapartePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    _contrapartes = "//div[contains(text(),'CONTRAPARTE')]"
    _que_buscar = "//*[@id='search']"
    _lupa = "//*[@class='sc-AxiKw fDcFlR']"
    _contrap_selecc = "//div[contains(text(),'DEFAULT DOXTOR')]"
    _path = "counterpart/"
    _path_count ="1"
    _por_vencer = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='number porvencer']"
    _vencidos = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='number vencidos']"
    _pais = "//*[@class='cards']//*[@class='sc-fznyAO cBMEdc card']//*[@name='DEFAULT DOXTOR']//*[@class='pais']"
    _busq_pais = "//*[@class='select__single-value css-1uccc91-singleValue']"
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
    _texto_busqueda_avanzada_num = "//div[contains(text(),'Filtrar sólo por número de documento')]"
    _texto_busqueda_conatel = "//div[contains(text(),'Filtrar sólo por Conatel:')]"
    _cerrar ="(//*[@stroke])[22]"
    _click_doc = "//*[@class='container']"

    def account_contraparte(self):
        self.elementClick(self._contrapartes, locatorType="xpath")
        return self.driver.current_url

    def account_buscar(self):
        self.elementClick(self._que_buscar, locatorType="xpath")
        self.elementClick(self._contraparte_buscar, locatorType="xpath")
        self.elementClick(self._lupa, locatorType="xpath")
        self.elementClick(self._contrap_selecc, locatorType="xpath")
        #self.text_to_validate = self.getText(self._contrap_selecc)
        #time.sleep(5)
        #self.getText(self._contrap_selecc, locatorType="xpath")
        return self.driver.current_url


    def contraparte_seleccionada(self):
        self.contraparte = self.getText(self._contrap_selecc, locatorType="xpath")
        return self.contraparte.text

    def seleccionar_busqueda_avanzada_num(self):
        self.elementClick(self._busqueda_avanzada, locatorType="xpath")
        self.elementClick(self._bus_por_num, locatorType="xpath")
        self.elementClick(self._boton_aplicar, locatorType="xpath")
        #text_to_validate = self.getText(self._texto_busqueda_avanzada_num, locatorType="xpath")
        titulo_busqueda = self.driver.find_element(By.XPATH, self._texto_busqueda_avanzada_num)
        return titulo_busqueda.text

    def cerrar_busqueda_avanzada(self):
        self.elementClick(self._cerrar, locatorType="xpath")

    def seleccionar_busqueda_conatel(self):
        self.elementClick(self._busqueda_avanzada, locatorType="xpath")
        self.elementClick(self._bus_conatel, locatorType="xpath")
        self.elementClick(self._boton_aplicar, locatorType="xpath")
        titulo_busqueda = self.driver.find_element(By.XPATH, self._texto_busqueda_conatel)
        return titulo_busqueda.text

    def click_documento(self):
        #self.elementClick(self._click_doc, locatorType="xpath")
        documentos_asociados = self.driver.find_element(By.XPATH, self._click_doc)
        return documentos_asociados.text