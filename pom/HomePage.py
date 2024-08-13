from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.new_post_button = (By.ID, ":r1:")

    def click_new_post(self):
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.new_post_button))
        self.driver.find_element(*self.new_post_button).click()
