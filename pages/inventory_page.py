from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_element = (By.CLASS_NAME, "inventory_item")
    product_button = (By.CLASS_NAME, "btn_inventory ")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_button = (By.CLASS_NAME, "shopping_cart_link")

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

    def add_first_product_to_cart(self):
        """
        Find the first product, click the add to cart button, send the product name

        No parameter

        Return:
            Product name, product quantity (text)
        """

        products = self.driver.find_elements(*self.product_element)
        first_product = products[0]

        first_product_name = first_product.find_element(*self.product_name)
        first_product_cta = first_product.find_element(*self.product_button)

        return first_product_name.text, first_product_cta

    def redirect_to_cart_page(self):
        """
            Perform click to cart button, redirect to cart page

            No parameter

            No return
        """
        cart_button_element = self.driver.find_element(*self.cart_button)
        cart_button_element.click()