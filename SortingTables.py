from selenium import webdriver
from selenium.webdriver.common.by import By
browsersortedveggie = []

driver = webdriver.Chrome(executable_path="C:/Users/faiz/Downloads/Udemy_Selenium-Practice/Selenium_Course/chromedriver-win64/chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on sorting buton at web
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#retrieve all veggie name
veggiewebelement = driver.find_elements(By.XPATH,"//tr/td[1]")

#will store all the veggie name in browsersortedveggie
for ele in veggiewebelement:
    browsersortedveggie.append(ele.text)

#print(browsersortedveggie)