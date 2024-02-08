import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome driver without local chromedriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)

#select all the elements with matching attribute
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print((len(countries)))

#Itterate for India in country and the click on that
for country in countries:
    if country.text == "India":
        country.click()
        break

#print attribute of manual input
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

driver.close()