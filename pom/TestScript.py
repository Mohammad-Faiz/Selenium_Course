import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from LoginPage import LoginPage
from HomePage import HomePage
from NewPostPage import NewPostPage

# Setup WebDriver
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://client-auth-dev.fanfix.dev/login")
driver.maximize_window()

# Login
login_page = LoginPage(driver)
login_page.enter_email("testqa@mailinator.com")
login_page.enter_password("123456789")
login_page.click_login()

# Create New Post
home_page = HomePage(driver)
home_page.click_new_post()

new_post_page = NewPostPage(driver)
new_post_page.click_free_post()
new_post_page.enter_caption("This post is done by Sania through Automation")
new_post_page.select_dropdown_option()
new_post_page.select_date()
new_post_page.click_ok()
new_post_page.click_post()

time.sleep(4)
driver.quit()
