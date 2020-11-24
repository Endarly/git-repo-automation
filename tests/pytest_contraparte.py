from pages.login_page import DoxtorLogin as LD
from pages.account_page import AccountPage as AP
from pages.contrapartes_page import ContrapartePage as CP
#from pages.contrapartes_pages_copia import ContrapartePageModificada as CPM
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
    password = "Viernes44*"
    driver = wd("chrome")
    _url = "http://10.92.114.78:3002/"
    _contraparte = "DEFAULT DOXTOR"
    _busqueda_avanzada_num = "Filtrar sólo por número de documento:"
    _busqueda_conatel = "Filtrar sólo por Conatel:"
    _counterpart = "counterpart"
    _id_counterpart = "/1"
    _documentos_asociados ="Este documento no tiene documentos asociados"
    _bus_pais_arg = "Argentina"
    _bus_tipo_contrato = "Contrato"
    _bus_tipo_adenda = "Adenda"
    _bus_tipo_carta_oferta = "Carta Oferta"
    _bus_tipo_convenio = "Convenio"
    _bus_tipo_poder = "Poder"
    _bus_tipo_escritura = "Escritura"
    _bus_tipo_Regulacion = "Regulación"
    _bus_tipo_Nota = "Nota"
    _bus_tipo_Resolucion = "Resolución"
    _plazo= "Fecha desde:"

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.driver =self.driver.getWebDriverInstance(self._url)
        self.ld = LD(self.driver)
        self.ap = AP(self.driver)
        self.cp = CP(self.driver)
        #self.dp = DP(self.driver)
        self.cpp = CPP(self.driver)
        self.rp = RP(self.driver)
        #self.cpm = CPM(self.driver)

    #@pytest.mark.run(order=1)
    def test_validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_validLogin started")
        self.log.info("*#" * 20)
        self.ld.login(self.email, self.password)
        assert (self.driver.current_url == self._url)
        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url+self._counterpart+self._id_counterpart)
        assert (self.cp.seleccionar_busqueda_avanzada_num() == self._busqueda_avanzada_num)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.seleccionar_busqueda_conatel() == self._busqueda_conatel)

        #assert (self.cp.account_contraparte() == self._url)
        #assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        #assert (self.cp.seleccionar_pais() == self._bus_pais_arg)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_contrato() == self._bus_tipo_contrato)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_adenda() == self._bus_tipo_adenda)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_carta_oferta() == self._bus_tipo_carta_oferta)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_convenio() == self._bus_tipo_convenio)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_poder() == self._bus_tipo_poder)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_escritura() == self._bus_tipo_escritura)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_regulacion() == self._bus_tipo_Regulacion)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_nota() == self._bus_tipo_Nota)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.tipo_documento_resolucion() == self._bus_tipo_Resolucion)

        assert (self.cp.account_contraparte() == self._url)
        assert (self.cp.account_buscar() == self._url + self._counterpart + self._id_counterpart)
        assert (self.cp.bus_plazo() == self._plazo)
