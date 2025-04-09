import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def supposed():
    return False

@pytest.mark.smokez
def test_open_web():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")
    assert "Swag" in driver.title
    assert supposed() == True

    time.sleep(3)
    driver.quit()
