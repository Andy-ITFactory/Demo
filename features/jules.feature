Feature: Jules login test

    Background:
      Given jules: user is on the login page


    @smoke
    Scenario Outline: Login 123
        When jules: user enters valid username "itfactory.ro@gmail.com" and valid password "<pass>"

    Examples:
      |pass|
      |password1|
      |password2|
      |password3|

    @smoke2
    Scenario: Login 1
        When jules: user enters valid username "itfactory.ro@gmail.com" and valid password "pass123"
