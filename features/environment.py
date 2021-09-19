from features.browser import Browser
from features.pages.jules_page import JulesPage


def before_all(context):

    # user credentials
    username = 'itfactory.ro@gmail.com'
    password = 'Start123!'

    context.browser = Browser()
    context.jules_page = JulesPage()

    context.jules_page.navigate_to_jules()


def after_all(context):
    context.browser.close()
