from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver without local chromedriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.linkedin.com/feed/")