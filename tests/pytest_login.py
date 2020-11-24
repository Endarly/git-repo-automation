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
    password = "Viernes44*"
    driver = wd("chrome")
    _url = "http://10.92.114.78:3002/"
    _Titulo_reporte= "Reportes"

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

        self.ap.account_documentos()
        assert (self.driver.current_url == self._url + self.ap._path)

        self.cp.account_contraparte()

        self.cp.account_buscar()
        assert (self.driver.current_url == self._url + self.cp._path + self.cp._path_count)

        self.dp.account_documento()
        assert (self.driver.current_url == self._url + self.dp._path)

        self.dp.account_buscar()
        assert (self.driver.current_url == self._url + self.dp._path_doc)

        self.cpp.account_colaprocesos()
        assert (self.driver.current_url == self._url + self.cpp._path)

        self.rp.account_reporte()
        assert (self.driver.current_url == self._url + self.rp._path)

        self.rp.reporte_titulo()
        assert (self.rp.reporte_titulo() == self._Titulo_reporte)
