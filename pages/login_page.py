from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "Email login is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTER), "Email register is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER_REPEAT), "Register repeat password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not present"

    def registration_new_user(self, email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        email_registration.send_keys(email)
        password_registration = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        password_registration.send_keys(password)
        password_registration_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_REPEAT)
        password_registration_repeat.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        self.browser.implicitly_wait(5)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM), \
            "Registration is not confirm!"
        self.browser.implicitly_wait(5)
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User is not autorized!"

