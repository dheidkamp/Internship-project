from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\dheid\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fcart%3Fapp-nav-type%3Dnone%26dc%3Ddf&prevRID=02D405R4CPRT5JW6ENNQ&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&ref_=cart_empty_sign_in&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo') #Amazon logo
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small') #Create account
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name') #Your name field
driver.find_element(By.CSS_SELECTOR, '#ap_email') #Email field
driver.find_element(By.CSS_SELECTOR, '#ap_password') #Password field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check') #Re-enter password
driver.find_element(By.CSS_SELECTOR, '#continue') #Continue button
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']") #Conditions of use
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']") #Privacy notice
driver.find_element(By.CSS_SELECTOR, "[href*='/ap/signin?']") #Sign in

print('Test Passed')

driver.quit()