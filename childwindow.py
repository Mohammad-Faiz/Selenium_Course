from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")

windowsopened = driver.window_handles

driver.find_element(By.LINK_TEXT,"Click Here").click()
print(driver.find_element(By.XPATH,"//h3").text)
windowsopened = driver.window_handles

driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.XPATH,"//h3").text)
driver.close()

driver.switch_to.window(windowsopened[0])

assert "Opening a new window" in driver.find_element(By.XPATH,"//h3").text