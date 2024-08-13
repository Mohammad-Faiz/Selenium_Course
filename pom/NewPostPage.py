from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class NewPostPage:
    def __init__(self, driver):
        self.driver = driver
        self.free_post_button = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[1]/div/div/button[2]")
        self.post_caption = (By.ID, "post-caption")
        self.dropdown = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div")
        self.dropdown_option = (By.XPATH, "//*[@id='ul-menu']/ul/li[2]")
        self.date_picker_button = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[2]/div[3]/div/div/button")
        self.next_month_button = (By.XPATH, "//button[@title='Next month']")
        self.ok_button = (By.XPATH, "/html/body/div[7]/div[2]/div/div[2]/button")
        self.post_button = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div[2]/div/div/div[3]/div[3]/button")

    def click_free_post(self):
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.free_post_button))
        self.driver.find_element(*self.free_post_button).click()

    def enter_caption(self, caption):
        self.driver.find_element(*self.post_caption).send_keys(caption)

    def select_dropdown_option(self):
        self.driver.find_element(*self.dropdown).click()
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.dropdown_option))
        self.driver.find_element(*self.dropdown_option).click()

    def select_date(self):
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.date_picker_button))
        self.driver.find_element(*self.date_picker_button).click()
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.next_month_button))
        self.driver.find_element(*self.next_month_button).click()

    def click_ok(self):
        WebDriverWait(self.driver, 12).until(EC.presence_of_element_located(self.ok_button))
        self.driver.find_element(*self.ok_button).click()

    def click_post(self):
        self.driver.find_element(*self.post_button).click()
