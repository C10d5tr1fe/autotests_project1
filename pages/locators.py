from selenium.webdriver.common.by import By


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

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[value='Add to basket']")
    PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    ADDED_PRODUCT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ADDED_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")