from selenium.webdriver.support.ui import WebDriverWait
from utils.waits import wait_for_clickable, wait_for_presence, wait_for_visibility

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)
    # locator is tuple, to extract it we are using * to unpack it
    # *("id", "element-id") == "id", "element-id"

    def type(self, locator, text):
        wait_for_visibility(self.driver, locator).send_keys(text)

    def click(self, locator):
        wait_for_visibility(self.driver, locator).click()