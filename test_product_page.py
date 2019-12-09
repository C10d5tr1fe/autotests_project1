from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()