import time

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import create_logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

logger = create_logger(__name__)

def test_checkout_page(driver, retrieve_config_data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    product_title, product_cta = inventory_page.add_first_product_to_cart()
    product_cta.click()
    inventory_page.redirect_to_cart_page()

    cart_page.click_checkout_button()

    checkout_page.fill_checkout_information("Daniel", "Tester", 12345)
    checkout_page.click_continue_button()
    assert checkout_page.validate_checkout_data(product_title)

    checkout_page.click_finish_button()
    assert checkout_page.validate_checkout_finish_data()



