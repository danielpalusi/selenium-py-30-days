from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    zip_postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    checkout_product_name = (By.CLASS_NAME, "inventory_item_name")
    finish_button = (By.ID, "finish")
    checkout_finish = (By.CLASS_NAME, "complete-header")

    def fill_checkout_information(self, first_name, last_name, postal):
        """
        Fill required fields on checkout page

        Parameter:
            Firstname, lastname, postal (text)

        No return
        """
        self.type(self.first_name_input, first_name)
        self.type(self.last_name_input, last_name)
        self.type(self.zip_postal_code_input, postal)

    def click_continue_button(self):
        self.click(self.continue_button)

    def validate_checkout_data(self, expected_data):
        """
        Retrieve checkout data on checkout page and compare it with expected data

        Parameter:
            Expected data (text)

        Return:
            Boolean
        """
        displayed_product_name = self.find(self.checkout_product_name)

        return displayed_product_name.text == expected_data

    def click_finish_button(self):
        self.click(self.finish_button)

    def validate_checkout_finish_data(self):
        """
        Retrieve finish data on checkout page and validate the value

        Parameter:
            Expected data (text)

        Return:
            Boolean
        """
        displayed_finish_wording = self.find(self.checkout_finish)

        return displayed_finish_wording.text == "Thank you for your order!"


