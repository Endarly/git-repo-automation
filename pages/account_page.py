from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    _path = "account/"
    _user_account_xpath = "//h3[contains(text(), 'Hi, Demo User')]"
    _account_link_xpath = "//*[@class ='dropdown dropdown-login dropdown-tab']"
    _logout_link_xpath = "//a[contains(text(), 'Logout')]"
    _newsletter_link_xpath = "//a[contains(text(), 'Newsletter')]"
    _newsletter_div_id = "newsletter"

    def account_name(self):
        remember_me= self.driver.find_element(By.XPATH,self._user_account_xpath)
        return remember_me.text

    def logout_action(self):
        account_link = self.driver.find_element(By.XPATH,self._account_link_xpath)
        account_link.click()
        logout_link = self.driver.find_element(By.XPATH,self._logout_link_xpath)
        logout_link.click()

    def newsletter_action(self):
        newsletter_link = self.driver.find_element(By.XPATH,self._newsletter_link_xpath)
        newsletter_link.click()

    def subscribe_class(self):
        newsletter_div = self.driver.find_element(By.ID,self._newsletter_div_id)
        return newsletter_div.get_attribute('class')
