import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#To open chrome without local chromedriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

#To open url
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

#To enter name, email, password and click checkbox
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("practice")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#DROPDOWN
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)


#Print success message after submit
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

#Check weather success word is present in message variable
assert "Success" in message
time.sleep(5)