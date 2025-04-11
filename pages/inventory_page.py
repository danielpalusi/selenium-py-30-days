from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    add_to_chart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    product_name = (By.CLASS_NAME, "inventory_item_name")

    def get_item_title(self):
        """
        Perform action to retrieve the product names

        No parameter

        Return:
            Text (str)
        """
        return [item.text for item in self.driver.find_elements(*self.product_name)]

    # def add_to_chart(self):
    #     """
    #     Perform add product to cart by click the "Add to chart" button
    #
    #     """
