from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class JulesPageElements(object):

    USER = '(//input)[1]'
    PASS = '(//input)[2]'
    LOGIN = '//button'


class JulesPage(Browser):
    # login page actions

    def navigate_to_jules(self):
        self.driver.get('https://jules.app/sign-in')

    def get_page_title(self):
        return self.driver.title

    def set_username(self, username):
        user_name_field = self.driver.find_element_by_xpath(JulesPageElements.USER)
        user_name_field.send_keys(username)

    def set_password(self, password):
        password_field = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, JulesPageElements.PASS))
        )
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(JulesPageElements.LOGIN).click()

    # step definition (agregare de pasi mici, care au logica)
    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
