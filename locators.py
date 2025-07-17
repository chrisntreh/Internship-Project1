from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')
driver.find_element(By.ID,'nav-logo-sprites')
driver.find_element(By.ID,'nav-link-accountList-nav-line-1').click()
driver.find_element(By.ID,'ap_email')
driver.find_element(By.ID,'continue')
driver.find_element(By.ID,'legalTextRow')
driver.find_element(By.XPATH,"//a [@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")
driver.find_element(By.XPATH,"//span [@class='a-expander-prompt']").click()
driver.find_element(By.ID,'auth-fpp-link-bottom')
driver.find_element(By.ID,'ap-other-signin-issues-link')
driver.find_element(By.ID,'createAccountSubmit')


sleep(10)