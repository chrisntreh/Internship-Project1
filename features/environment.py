from ssl import Options
from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    #
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    #
    # context.driver = webdriver.Chrome(service=service, options=options)

    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/reelly_internship_test.feature

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)




    bs_user = "christopherntreh_lzwbTy"
    bs_key = "oPTxGiAq26rkyw4T4CwF"
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'


    options = Options()
    bstack_options = {
        'os' : 'OS X',
        'osVersion' : 'Sonoma',
        'browserName': 'chrome',
        'sessionName' : 'scenario_name',
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver= webdriver.Remote(command_executor=url, options=options)



    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)





def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
