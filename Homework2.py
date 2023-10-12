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
driver.get('https://www.amazon.com')

#Click on Orders button
driver.find_element(By.XPATH, "//span[@class='nav-line-2' and text()='& Orders']").click()

#Verification
expected_result = 'Sign in'
actual_text = driver.find_element(By. XPATH, "//h1[@class='a-spacing-small']").text

assert actual_text == expected_result, f'expected {expected_result} but got {actual_result}'

#Verify email field is present
driver.find_element(By.ID, 'ap_email')

