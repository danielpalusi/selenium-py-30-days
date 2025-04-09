from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service_object = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_object)

driver.get("https://www.saucedemo.com/")
print(driver.title)

time.sleep(3)

driver.quit()
