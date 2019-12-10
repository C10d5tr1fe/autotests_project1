from .base_page import BasePage
from .locators import ProductPageLocators
import time

#класс для страницы продукта, наследуем класс от  BasePage
class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_add_basket()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_add_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_basket.click()
        self.browser.implicitly_wait(5)
        self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        time.sleep(2)

    def not_should_to_be_disappeared__after_add_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_basket.click()
        self.browser.implicitly_wait(5)
        self.solve_quiz_and_get_code()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        time.sleep(2)

    def should_be_product_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            "Add Basket button not find"
        assert self.is_element_present(*ProductPageLocators.PRODUCT), \
            "Product not find"
        assert self.is_element_present(*ProductPageLocators.PRICE), \
            "Price not find"
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_basket.click()
        self.browser.implicitly_wait(5)
        self.solve_quiz_and_get_code()

        self.browser.implicitly_wait(5)
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT), \
            "Added product not find"
        assert self.is_element_present(*ProductPageLocators.ADDED_PRICE), \
            "Added price not find"
        self.browser.implicitly_wait(5)

        product = self.browser.find_element(*ProductPageLocators.PRODUCT)
        product_text = product.text
        print(f"Product name is '{product_text}'")
        product_added = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)
        product_added_text = product_added.text
        print(f"Product name at basket is '{product_added_text}'")
        assert product_text == product_added_text, f"Wrong name product at basket!, now {product_added_text}"
        time.sleep(2)

        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_text = price.text
        print(f"Price is '{price_text}'")
        price_added = self.browser.find_element(*ProductPageLocators.ADDED_PRICE)
        price_added_text = price_added.text
        print(f"Price at basket is '{price_added_text}'")
        assert price_text == price_added_text, f"Wrong  price at basket!, now {price_added_text}"
        time.sleep(2)