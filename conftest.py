import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_parser import config
from utils.logger import create_logger


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

logger = create_logger(__name__)

@pytest.hookimpl()
def pytest_runtest_protocol(item, nextitem):
    logger.info(f"Starting test: {item.nodeid} 🚀🚀")

    result = nextitem

    logger.info(f"Test finished: {item.nodeid} ⛳⛳")

    return result


