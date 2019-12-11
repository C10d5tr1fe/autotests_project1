from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        registration_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password =  "NewPassword123"
        registration_page.registration_new_user(email, password)

    @pytest.mark.skip
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина

    @pytest.mark.parametrize('link', urls)
    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser, link):
        #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_product_page()

    @pytest.mark.parametrize('link', urls)
    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        #link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                        # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message_after_add_basket()

    @pytest.mark.parametrize('link', urls)
    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser,link):
        #link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                        # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.parametrize('link', urls)
    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser,link):
        #link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                        # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.not_should_to_be_disappeared__after_add_basket()

    @pytest.mark.skip
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_basket_page()  # выполняем метод страницы - переходим на страницу логина
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.empty_basket()

    #@pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_product_page()

    #@pytest.mark.skip
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message_after_add_basket()