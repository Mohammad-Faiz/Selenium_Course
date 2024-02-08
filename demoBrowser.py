from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver without local chromedriver
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)


driver = webdriver.Chrome(executable_path="C:/Users/faiz/Downloads/Udemy_Selenium-Practice/Selenium_Course/chromedriver-win64/chromedriver.exe")

driver.get("https://www.linkedin.com/feed/")

driver.close()