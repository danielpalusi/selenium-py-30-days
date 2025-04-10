from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super.__init__(driver)

    def login(self,  username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)