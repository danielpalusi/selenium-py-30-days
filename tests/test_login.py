from pages.login_page import LoginPage
import time

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
    time.sleep(3)