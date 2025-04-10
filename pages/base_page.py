from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    # expected_conditions-visibility_of_element_located needs full tuple of locator
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))