import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(Options())
driver.implicitly_wait(5)
driver.get("https://client-auth-dev.fanfix.dev/login")
driver.maximize_window()

#Login
driver.find_element(By.ID,"email").send_keys("testqa@mailinator.com")
driver.find_element(By.ID,"password").send_keys("123456789")
wait=WebDriverWait(driver,12)

wait.until(expected_conditions.presence_of_element_located((By.ID,":r2:")))
driver.find_element(By.ID,":r2:").click()

time.sleep(3)

#NewPost
wait.until(expected_conditions.presence_of_element_located((By.ID,":r1:")))
driver.find_element(By.ID,":r1:").click()

#free post
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[1]/div/div/button[2]")))
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[1]/div/div/button[2]").click()
time.sleep(2)
driver.find_element(By.ID,"post-caption").send_keys("This post is done by Faiz through Automation")
time.sleep(3)

#Dropdown
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='ul-menu']/ul/li[2]")))
driver.find_element(By.XPATH,"//*[@id='ul-menu']/ul/li[2]").click()

#Calendar
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[2]/div[3]/div/div/button")))
date_picker = driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[2]/div[3]/div/div/button")
date_picker.click()

#Month
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@title='Next month']")))
month_button= driver.find_element(By.XPATH,"//button[@title='Next month']")
month_button.click()

#days
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@title='Next month']")))
day_1=driver.find_element(By.XPATH,"//button[@title='Next month']")
day_1.click()
time.sleep(2)
#Click Ok
driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[2]/button").click()

#Click Post
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[3]/button").click()

time.sleep(4)
driver.quit()