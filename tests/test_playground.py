from pages.login_page import LoginPage
import time

# def test_open_web(driver):
#     driver.get("https://www.saucedemo.com")
#     assert "Swag" in driver.title
#
#     time.sleep(3)
#     driver.quit()

def test_screenshot(driver):
    """
    This is only playground to trigger the screenshot file

    Parameter:
    driver

    No return
    """
    login_page = LoginPage(driver)
    login_page.go_to("https://example.com")

    assert "Example Domaindo" in driver.title
