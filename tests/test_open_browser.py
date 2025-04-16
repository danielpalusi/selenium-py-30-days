import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot
import time

def test_open_web(driver):
    driver.get("https://www.saucedemo.com")
    assert "Swag" in driver.title

    time.sleep(3)
    driver.quit()

def test_screenshot(driver):
    """
    This is only playground to trigger the screenshot file

    Parameter:
    driver

    No return
    """
    login_page = LoginPage(driver)
    login_page.go_to("https://example.com")
    take_screenshot(driver, "example_error")

    assert "Example Domain" in driver.title
