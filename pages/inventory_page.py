from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_item_title(self):
        """
        Perform action to retrieve the product names

        No parameter

        Return:
            Text (str)
        """
        return [item.text for item in self.driver.find_elements(*self.product_name)]

    def add_to_chart(self):
        """
        Perform add product to cart by click the "Add to chart" button

        No parameter

        Return:
            Cart badge amount
        """
        self.click(self.backpack_add_to_cart_button)
        chart_badge = self.driver.find_element(*self.cart_badge)
        return chart_badge.text