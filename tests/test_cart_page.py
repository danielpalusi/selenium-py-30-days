from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import create_logger

logger = create_logger(__name__)

def test_cart_page(driver, retrieve_config_data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    product_title, product_cta = inventory_page.add_first_product_to_cart()
    product_cta.click()

    inventory_page.redirect_to_cart_page()

    assert cart_page.check_product_on_cart(product_title)



