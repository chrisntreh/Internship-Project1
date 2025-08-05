from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class NavigationFilterPage(BasePage):
    #SECONDARY_MENU_LOCATOR = (By.XPATH, "//a[@href='/secondary-listings']")
    # SECONDARY_MENU_LOCATOR = (By.CSS_SELECTOR, 'a[class*="menu-button-block"][href="/secondary-listings"]')
    VERIFY_THE_RIGHT_PAGE_OPEN_LOCATOR = (By.XPATH, "//div[@class='verified-section']")
    FILTER_BUTTON_LOCATOR = (By.XPATH, "//div[@class='filter-text']")
    WANT_TO_BUY_CHECKBOX_LOCATOR = (By.XPATH, "//div[@wized='ListingTypeBuy']")
    APPLY_FILTER_BUTTON_LOCATOR = (By.XPATH, "//a[@class='button-filter w-button']")
    DEAL_CARDS_LOCATOR = (By.XPATH, "//div[@wized='saleTagBoxMLS']")
    SECONDARY_MENU_LOCATOR = (By.XPATH, "//button[@class='pb-5 text-sm font-semibold transition-all border-b-2 border-transparent whitespace-nowrap text-muted-foreground']")

    def go_to_secondary_menu(self):
        sleep(30)
        self.click(*self.SECONDARY_MENU_LOCATOR)
        sleep(5)

    def verify_the_right_page(self):
        sleep(10)
        url = self.driver.current_url
        assert url == 'https://soft.reelly.io/secondary-listings'


    def open_filters(self):
        sleep(5)
        self.click(*self.FILTER_BUTTON_LOCATOR)

    def select_want_to_buy(self):
        sleep(3)
        self.click(*self.WANT_TO_BUY_CHECKBOX_LOCATOR)

    def apply_filters(self):
        sleep(3)
        self.click(*self.APPLY_FILTER_BUTTON_LOCATOR)

    def verify_want_to_buy(self):
        sleep(3)
        cards = self.find_elements(*self.DEAL_CARDS_LOCATOR)
        for cards in cards:
            assert 'Want to buy' in cards.text, f' Missing tag in card: {cards.text}'