from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > span > a")

class BasketPageLocators():
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_LOGIN = (By.ID, "id_login-username")
    PASSWORD_LOGIN = (By.ID, "id_login-password")
    EMAIL_REGISTER = (By.ID, "id_registration-email")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    PASSWORD_REGISTER = (By.ID, "id_registration-password1")
    PASSWORD_REGISTER_REPEAT = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_CONFIRM = (By.XPATH, "//div[@id='messages']/div[1]/div")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[value='Add to basket']")
    PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    ADDED_PRODUCT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ADDED_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
