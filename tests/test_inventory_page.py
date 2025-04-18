from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_retrieve_inventory_product_name(driver, retrieve_config_data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    result = inventory_page.get_item_title()

    print(result)

    assert len(result) > 0

def test_add_product_to_chart(driver, retrieve_config_data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    cart_badge_amount = inventory_page.add_to_chart()
    assert int(cart_badge_amount) > 0