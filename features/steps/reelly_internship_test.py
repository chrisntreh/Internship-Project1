# git add .
# git commit -m "your message"
# git push
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('the user Open Relly main page')
def open_main_page(context):
    context.app.main_page.open()


@when('user signs in')
def sign_up_page(context):
    context.app.sign_in_page.enter_email()
    context.app.sign_in_page.enter_password()
    context.app.sign_in_page.sign_in_button()


@when('user Click on the Secondary to the left')
def go_to_secondary_menu(context):
    context.app.Navigation_Filter_Page.go_to_secondary_menu()


@when('verify the right page opens')
def open_filters(context)
    context.app.Navigation_Filter_Page.open_filters()

@when('user click on filters')
def verify_the_right_page(context)
    context.app.Navigation_Filter_Page.verify_the_right_page()


@then('filter the products by want_to_buy')
def select_want_to_buy(context):
    context.app.Navigation_Filter_Page.select_want_to_buy()


@when('user click on apply filter')
def apply_filters(context):
    context.app.Navigation_Filter_Page.apply_filters()


@then('Verify all cards have a want_to_buy tag')
def verify_want_to_buy(context):
    context.app.Navigation_Filter_Page.verify_want_to_buy()




