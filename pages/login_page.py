from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.curret_url(), "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "Email login is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTER), "Email register is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER_REPEAT), "Register repeat password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not present"