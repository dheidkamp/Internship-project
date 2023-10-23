from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # CHROME BROWSER
    # service = Service(executable_path=r'C:\Users\dheid\python-selenium-automation\chromedriver.exe')
    # # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service)

    # # FIREFOX BROWSER
    # service = Service(executable_path=r'\Users\dheid\OneDrive\Desktop\Automation_Internship\geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    # # HEADLESS MODE CHROME
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path=r'C:\Users\dheid\python-selenium-automation\chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # # # HEADLESS MODE FIREFOX
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path=r'\Users\dheid\OneDrive\Desktop\Automation_Internship\geckodriver')
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'davidheidkamp_niuIE7'
    bs_key = 'iAiL5eUMUEz8rsu2osoQ'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Big Sur',
        'browserName': 'Chrome',
        'sessionName': 'Registration_Page'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
