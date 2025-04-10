from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def login(self,  username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)