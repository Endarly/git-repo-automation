from pages.login_page import DoxtorLogin as LD
from pages.account_page import AccountPage as AP
from pages.contrapartes_page import ContrapartePage as CP
from pages.contrapartes_pages_copia import ContrapartePageModificada as CPM
#from pages.documentos_page import DocumentosPage as DP
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
    _busqueda_avanzada_num = "Filtrar sólo por número de documento:"
    _busqueda_conatel = "Filtrar sólo por Conatel:"

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.driver =self.driver.getWebDriverInstance(self._url)
        self.ld = LD(self.driver)
        self.ap = AP(self.driver)
        self.cp = CP(self.driver)
        #self.dp = DP(self.driver)
        self.cpp = CPP(self.driver)
        self.rp = RP(self.driver)
        self.cpm = CPM(self.driver)

    #@pytest.mark.run(order=1)
    def test_validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_validLogin started")
        self.log.info("*#" * 20)
        self.ld.login(self.email, self.password)
        assert (self.driver.current_url == self._url)

        #self.cp.account_contraparte()
        #assert (self.driver.current_url == self._url)

        self.cpm.account_contraparte_modificada()
        assert (self.driver.current_url == self._url)

        self.cpm.account_buscarm()
        assert (self._contraparte == self.cpm.contraparte_seleccionadam())

        assert (self.cpm.seleccionar_busqueda_avanzada_numm() == self._busqueda_avanzada_num)

        self.cpm.cerrar_busqueda_avanzadam()

        self.cpm.account_contraparte_modificada()
        assert (self._contraparte == self.cpm.contraparte_seleccionadam())


        assert (self.cp.seleccionar_busqueda_conatelm() == self._busqueda_conatel)

