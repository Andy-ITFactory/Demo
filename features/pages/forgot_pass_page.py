from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class JulesPageElements(object):

    EMAIL_INPUT = '(//input)[1]'
    SEND_EMAIL_BTN = '(//input)[2]'


class JulesPage(Browser):
    # login page actions

    def navigate_to_jules(self):
        self.driver.get('https://jules.app/forgot-password')

    def get_page_title(self):
        return self.driver.title

