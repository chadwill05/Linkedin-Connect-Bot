from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

# Replace this with the path you copied
chromedriver_path = "/Users/chad/Desktop/Web development/chromedriver"

# Create a Service object
service = Service(executable_path=chromedriver_path)

# Pass the Service object to the webdriver.Chrome constructor
driver = webdriver.Chrome(service=service)

driver.get("https://linkedin.com")

time.sleep(2)
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys("")
password.send_keys("")

time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.get("https://www.linkedin.com/search/results/people/?keywords=cash%20advance&origin=SWITCH_SEARCH_VERTICAL&page=5&sid=!MX")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(4)