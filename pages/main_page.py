from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


#наследуем класс от  BasePage
class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)