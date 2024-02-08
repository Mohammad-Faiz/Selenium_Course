from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome driver without local chromedriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#store all the checkbox element in variable
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

#itterate the desired option in checkbox and click that
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break

driver.close()