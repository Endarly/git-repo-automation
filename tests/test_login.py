from pages.home_phptravels import HomePhpTravels as HPT
from pages.login_phptravels import  LoginPhpTravels as LPT
from pages.account_page import AccountPage as AP
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.maximize_window()
_url = "https://www.phptravels.net/"
driver.get(_url)
email = "user@phptravels.com"
password = "demouser"

def testLogin():
   homeTest = HPT(driver)
   homeTest.login()
   loginTest=LPT(driver)
   loginTest.login(email, password)
   accountTest=AP(driver)
   accountName= "Hi, Demo User"

   assert (accountTest.account_name()==accountName)
   assert (driver.current_url == _url+accountTest._path)

   accountTest.newsletter_action()
   assert ("active" in accountTest.subscribe_class())

   accountTest.logout_action()
   assert (driver.current_url == _url+loginTest._path)

testLogin()
driver.quit()