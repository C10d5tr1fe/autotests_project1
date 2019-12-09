from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


#наследуем класс от  BasePage
class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"