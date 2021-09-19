from behave import *
from nose.tools import assert_true


# navigate to gmail using the url set in login_page.py
# if title is 'Gmail' then navigation was successful
@given('jules: user is on the login page')
def step_impl(context):
    context.jules_page.navigate_to_jules()

# valid username and valid password parameters are set in login.feature
@when('jules: user enters valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.jules_page.login(username, password) # login
    # search
    # add prop page 1
    # add prop 2