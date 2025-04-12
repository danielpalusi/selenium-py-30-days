from pages.login_page import LoginPage
from utils.logger import create_logger
from utils.config_parser import config
from pages.inventory_page import InventoryPage

logger = create_logger(__name__)

def test_retrieve_inventory_product_name(driver):
    logger.info("Starting inventory test - Retrieve product name 🚀🚀")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    url = config['base_url']
    username = config['username']
    password = config['password']

    login_page.go_to(url)
    login_page.login(username, password)

    result = inventory_page.get_item_title()

    print(result)

    assert len(result) > 0

    logger.info("Inventory test - Retrieve product name finished ⛳⛳")

def test_add_product_to_chart(driver):
    # this code DRY
    logger.info("Starting inventory test - Retrieve product name 🚀🚀")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    url = config['base_url']
    username = config['username']
    password = config['password']

    login_page.go_to(url)
    login_page.login(username, password)

    cart_badge_amount = inventory_page.add_to_chart()
    assert int(cart_badge_amount) > 0

