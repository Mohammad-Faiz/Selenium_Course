import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome driver without local chromedriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

#global wait
driver.implicitly_wait(5)

#open url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Enter prompt in search bar
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("Ber")
#click search button
driver.find_element(By.XPATH,"//button[@class='search-button']").click()

#it will store the number of result
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")

#count number of result
count = len(results)
print(count)
assert count > 0

#It will click add to cart for every result
for result in results:
    result.find_element(By.XPATH,"div/button").click()

#click to cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#click to proceed to checkout
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
#apply promocode
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
#click on apply promocode
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))


#print code applied
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)