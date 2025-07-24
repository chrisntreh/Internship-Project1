from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.navigation_filter_page import NavigationFilterPage
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.navigation_filter_page = NavigationFilterPage(driver)

