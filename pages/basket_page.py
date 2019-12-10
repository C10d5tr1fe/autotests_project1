from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Item in basket"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "No empty massage"