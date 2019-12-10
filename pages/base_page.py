import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():

    def __init__(self, browser, url: RemoteWebDriver, timeout = 10):
        self.browser = browser                 #конструктор окна браузера
        self.url = url                         #конструктор ссылки
        self.browser.implicitly_wait(timeout)  #команда для неявного ожидания со значением по умолчанию в 10

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):  #метод is_element_present, в котором будем перехватывать исключение
        try:                                  #в него будем передавать два аргумента: как (how) искать (css, id, xpath и тд) и что(what) искать (строку-селектор).
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4): #метод is_not_element_present, который проверяет, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
