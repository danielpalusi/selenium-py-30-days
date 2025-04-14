import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_parser import config

@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Provide the driver to the test
    yield driver

    #Teardown
    driver.quit()

@pytest.fixture()
def retrieve_config_data():
    """
    Retrieve config data from yaml file

    No parameter

    Return value:
    Text
    """

    # return is dict, so we can easily access it
    # dict like object in js
    url = config['base_url']
    username = config['username']
    password = config['password']

    return url, username, password
