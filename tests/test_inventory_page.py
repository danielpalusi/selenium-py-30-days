from pages.login_page import LoginPage
from utils.logger import create_logger
from pages.inventory_page import InventoryPage

logger = create_logger(__name__)

def test_retrieve_inventory_product_name(driver, retrieve_config_data):
    logger.info("Starting inventory test - Retrieve product name 🚀🚀")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    result = inventory_page.get_item_title()

    print(result)

    assert len(result) > 0

    logger.info("Inventory test - Retrieve product name finished ⛳⛳")

def test_add_product_to_chart(driver, retrieve_config_data):
    # this code DRY
    logger.info("Starting inventory test - Retrieve product name 🚀🚀")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    cart_badge_amount = inventory_page.add_to_chart()
    assert int(cart_badge_amount) > 0

