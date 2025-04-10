from pages.login_page import LoginPage
import time
from utils.config_parser import config

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    # return is dict, so we can easily access it
    # dict like object in js
    print(config['base_url'])
    print(config['password'])

    time.sleep(3)