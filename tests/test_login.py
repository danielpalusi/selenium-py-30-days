from pages.login_page import LoginPage
import time
from utils.config_parser import config

def test_login(driver):
    login_page = LoginPage(driver)

    # return is dict, so we can easily access it
    # dict like object in js
    url = config['base_url']
    username = config['username']
    password = config['password']

    login_page.go_to(url)
    login_page.login(username, password)

    assert "inventory" in driver.current_url

    time.sleep(3)