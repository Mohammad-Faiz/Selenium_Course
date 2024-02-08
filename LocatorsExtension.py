import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#To open chrome without local chromedriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

#To open url
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#Travel from parent --> child to create xpath
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")

#Travel from parent --> child to create css selector
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("abcdef")

#css selector using id
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("abcdef")

#manual created xpath //tagname[@attribute='value']
#driver.find_element(By.XPATH, "//button[@type='submit']").click()

#xpath when no attribute is given and only text is present
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(5)
driver.close()
