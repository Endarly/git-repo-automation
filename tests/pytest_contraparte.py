from pages.login_page import DoxtorLogin as LD
from pages.account_page import AccountPage as AP
from pages.contrapartes_page import ContrapartePage as CP
from pages.documentos_page import DocumentosPage as DP
from pages.cola_procesos_page import ColaProcesosPage as CPP
from pages.reportes_page import ReportePage as RP
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory as wd
import time

@pytest.mark.usefixtures()
class LoginTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    email = "EXB30522"
    password = "Viernes43*"
    driver = wd("chrome")
    _url = "http://10.92.114.78:3002/"
    _contraparte = "DEFAULT DOXTOR"
    _busqueda_avanzada = "Búsqueda avanzada:"

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.driver =self.driver.getWebDriverInstance(self._url)
        self.ld = LD(self.driver)
        self.ap = AP(self.driver)
        self.cp = CP(self.driver)
        self.dp = DP(self.driver)
        self.cpp = CPP(self.driver)
        self.rp = RP(self.driver)

    #@pytest.mark.run(order=1)
    def test_validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_validLogin started")
        self.log.info("*#" * 20)
        self.ld.login(self.email, self.password)
        assert (self.driver.current_url == self._url)

        self.cp.account_contraparte()
        assert (self.driver.current_url == self._url)

        self.cp.account_buscar()
        #assert ((self.driver) == self._contraparte)
        assert (self._contraparte == self.cp.contraparte_seleccionada())

        #self.cp.seleccionar_contraparte()
        #assert (self.driver.current_url == self._url + self.cp._path + self.cp._path_count)

        #self.cp.seleccionar_busqueda_avanzada()
        assert (self.cp.seleccionar_busqueda_avanzada() == self._busqueda_avanzada)
        #assert (self._busqueda_avanzada == self.cp._texto_busqueda_avanzada())

        #self.cp.contraparte_seleccionada()
        #assert (self._contraparte == self.cp.contraparte_seleccionada())

        #este sirve para comparar pero cuando ya está la contraparte seleccionda
        #assert (self.driver.current_url == self._url + self.cp._path + self.cp._path_count)


        #assert (self.driver.current_url() == self._contraparte)

        #self.cp.contraparte_seleccionada()
        #assert (self.driver.current_url == self._url + self.cp._path + self.cp._path_count)


        #assert (self.driver.current_url == self._url + self.cp._path + self.cp._path_count)


        #self.cp.account_