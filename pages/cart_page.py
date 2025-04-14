from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    product_name_text = (By.CLASS_NAME, "inventory_item_name")
    product_quantity = (By.CLASS_NAME, "cart_quantity")

    def check_product_on_cart(self):
        """
        Check product name and product quantity

        No parameter

        Return:
            Product name and quantity (text)
        """
        product_name_element = self.driver.find_element(*self.product_name_text)
        product_quantity = self.driver.find_element(*self.product_quantity)

        return product_name_element.text, product_quantity.text