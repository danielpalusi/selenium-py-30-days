from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    product_name_text = (By.CLASS_NAME, "inventory_item_name")
    product_quantity = (By.CLASS_NAME, "cart_quantity")
    checkout_button = (By.ID, "checkout")

    def check_product_on_cart(self, expected_product_name):
        """
        Check product name and product quantity

        No parameter

        Return:
            Boolean
        """

        product_name_text = self.find(self.product_name_text).text
        product_quantity_text = self.find(self.product_quantity).text

        print(product_quantity_text)

        return product_name_text == expected_product_name and int(product_quantity_text) >= 1

    def click_checkout_button(self):
        self.click(self.checkout_button)