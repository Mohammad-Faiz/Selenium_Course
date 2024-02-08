from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

#chrome driver without local chromedriver
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

action = ActionChains(driver)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()