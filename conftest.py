import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Provide the driver to the test
    yield driver

    #Teardown
    driver.quit()
