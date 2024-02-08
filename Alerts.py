import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome driver without local chromedriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
name = "faiz"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
alert.accept()
assert name in alerttext