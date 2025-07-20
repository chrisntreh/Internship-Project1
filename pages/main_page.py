from pages.base_page import BasePage


class MainPage(BasePage):
    REELY_PAGE = 'https://soft.reelly.io'

    def open(self):
        self.open_url(self.REELY_PAGE)
