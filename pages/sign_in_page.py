from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_LOCATOR = (By.XPATH, "//input[@id='email-2']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@id='field']")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//a[@class='login-button w-button']")
    EMAIL = "ntrehchris@gmail.com"
    PASSWORD = "313102@Ckn33"
    OFF_PLAN = (By.CSS_SELECTOR, 'div[wized*="mobileMenu"] a[wized="newOffPlanLink"]')


    def enter_email(self):
        self.input_text(self.EMAIL, *self.EMAIL_LOCATOR)

    def enter_password(self):
        self.input_text(self.PASSWORD, *self.PASSWORD_LOCATOR)

    def click_continue(self):
        self.click(*self.CONTINUE_BUTTON_LOCATOR)
        sleep(10)

    def click_off_plan(self):
        sleep(10)
        self.click(*self.OFF_PLAN)
