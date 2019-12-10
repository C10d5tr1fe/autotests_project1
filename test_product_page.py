from .pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()

@pytest.mark.parametrize('link', urls)
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    #link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message_after_add_basket()

@pytest.mark.parametrize('link', urls)
@pytest.mark.skip
def test_guest_cant_see_success_message(browser,link):
    #link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()

@pytest.mark.parametrize('link', urls)
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    #link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.not_should_to_be_disappeared__after_add_basket()