from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SecondaryPage(BasePage):
     SECONDARY_MENU_LOCATOR = (By.XPATH, "//div[@class='g-menu-text']")
     VERIFY_THE_RIGHT_PAGE_OPEN_LOCATOR = (By.XPATH, "//div[@class='verified-section']")
     FILTER_BUTTON_LOCATOR = (By.XPATH, "//div[@class='filter-text']")
     WANT_TO_BUY_CHECKBOX_LOCATOR = (By.XPATH, "//div[@class='switcher-button active']")
     APPLY_FILTER_BUTTON_LOCATOR = (By.XPATH, "//a[@class='button-filter w-button']")
     DEAL_CARDS_LOCATOR = (By.XPATH, "//div[@class='w-layout-grid listing-grid']")

     def go_to_secondary_menu(self):
         self.click(self.SECONDARY_MENU_LOCATOR)

    def verify_the_right_page(self):
        self.click(self.VERIFY_THE_RIGHT_PAGE_OPEN_LOCATOR)

    def open_filters(self)
        self.click_element(*self.FILTER_BUTTON_LOCATOR)

    def select_want_to_buy(self):
        self.click_element(*self.WANT_TO_BUY_CHECKBOX_LOCATOR)

    def apply_filters(self):
        self.click_element(*self.APPLY_FILTER_BUTTON_LOCATOR)

    def verify_want_to_buy(self):
        cards = self.find_elements(*self.DEAL_CARDS_LOCATOR)
        for cards in cards:
            assert 'want to buy' in cards.text, f' Missing tag in card: {cards.text}'