from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time

email = "example@gmail.com"
password = "123456789"

driver = webdriver.Chrome()
os.environ['PATH'] += "E:\Selenium Driver"

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3645453265&f_AL=true&f_JT=P&geoId=102713980&keywords=python%20developer&location=India&refresh=true")

sign_in_button = driver.find_element("link text","Sign in")

sign_in_button.click()

email_input = driver.find_element("name","session_key")
email_input.send_keys(email)
email_input.send_keys(Keys.TAB)

pass_input = driver.find_element("name","session_password")
pass_input.send_keys(password)
pass_input.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()