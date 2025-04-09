import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_open_web(driver):
    driver.get("https://www.saucedemo.com")
    assert "Swag" in driver.title

    time.sleep(3)
    driver.quit()
