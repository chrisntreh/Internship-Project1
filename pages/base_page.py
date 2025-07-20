from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)


    def find_element(self,*locator):
       return self.driver.find_element(*locator)



    def find_elements(self,*locator):
       return self.driver.find_elements(*locator)



    def click(self, *locator):
        self.driver.find_element(*locator).click()



    def input_text(self, text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window_handle(self):
        window = self.driver.current_window_handle
        print('Current window ', window)
        return window

    def switch_to_new_window(self):
        sleep(5)
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All windows ', all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Current window ', self.driver.current_window_handle)