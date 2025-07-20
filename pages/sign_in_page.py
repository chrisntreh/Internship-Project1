from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_LOCATOR = (By.XPATH, "//input[@ID='email-2']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@ID='field']")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//a[@class='login-button w-button']")

    PASSWORD = ""
    def enter_email(self, email):
        self.input_text(self.email, *self.EMAIL_LOCATOR)

    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD_LOCATOR)

    def click_continue(self, continue_button):
        self.click_continue(self.CONTINUE_BUTTON_LOCATOR)