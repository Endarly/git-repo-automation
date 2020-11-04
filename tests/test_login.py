from pages.login_page import DoxtorLogin as LD
from pages.account_page import AccountPage as AP
from pages.contrapartes_page import ContrapartePage as CP
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
url= "http://10.92.114.78:3002/"

driver.implicitly_wait(30)
driver.maximize_window()
driver.get(url)

def testLogin():
    loginTest=LD(driver)
    loginTest.login()

    #accounTest=AP(driver)
    #accountName="¿Qué necesitas buscar?"
    #assert (accounTest.account_user()==accountName)

    get_url=driver.current_url
    validate_account_url="http://10.92.114.78:3002/"
    assert (get_url == validate_account_url)
    print(get_url)

    contraparteTest = CP(driver)
    contraparteTest.account_contraparte()
    get_url=driver.current_url
    validate_account_url_contraparte="http://10.92.114.78:3002/"
    assert (get_url == validate_account_url_contraparte)

    documentosTest = AP(driver)
    documentosTest.account_documentos()
    get_url=driver.current_url
    validate_account_url_documento="http://10.92.114.78:3002/all_documents"
    assert  (get_url == validate_account_url_documento)
    time.sleep(3)

    coladeprocesosTest = AP(driver)
    coladeprocesosTest.account_colaprocesos()
    get_url=driver.current_url
    validate_account_url_colaprocesos ="http://10.92.114.78:3002/process_stack"
    assert (get_url == validate_account_url_colaprocesos)
    time.sleep(3)

    reportesTest = AP(driver)
    reportesTest.account_reportes()
    get_url=driver.current_url
    validate_account_url_reportes = "http://10.92.114.78:3002/reports"
    assert (get_url == validate_account_url_reportes)
    time.sleep(3)

    ajustesTest = AP(driver)
    ajustesTest.account_ajustes()
    get_url=driver.current_url
    validate_account_url ="http://10.92.114.78:3002/settings"
    assert  (get_url == validate_account_url)
    time.sleep(3)

    contraparteTest = CP(driver)
    contraparteTest.account_contraparte()
    time.sleep(3)

    quebuscarTest = CP(driver)
    quebuscarTest.account_buscar()
    get_url=driver.current_url
    validate_account_url = "http://10.92.114.78:3002/counterpart/1"
    assert (get_url == validate_account_url)
    time.sleep(3)

testLogin()
driver.quit()