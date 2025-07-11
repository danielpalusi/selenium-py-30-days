import pytest

from conftest import retrieve_config_data
from pages.login_page import LoginPage
from utils.logger import create_logger
from utils.config_parser import config

logger = create_logger(__name__)

def test_login(driver, retrieve_config_data):
    """
    Perform login process, go to url then insert credentials

    Parameter:
    driver
    retrieve_config_data (text)

    No return
    """
    login_page = LoginPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    assert "inventory" in driver.current_url

@pytest.mark.negative
def test_invalid_login(driver,retrieve_config_data):
    """
    Perform login process, go to url then insert invalid credentials

    Parameter:
    driver
    retrieve_config_data (text)

    No return
    """

    login_page = LoginPage(driver)

    # need to use the parameterize method
    url, _, _ = retrieve_config_data
    login_page.go_to(url)
    login_page.login("username", "password")

    assert "inventory" not in driver.current_url

@pytest.mark.parametrize("username, password", [(user["username"], user["password"]) for user in config["invalid_users"]])
def test_login_with_parametrized(driver, retrieve_config_data, username, password):
    login_page = LoginPage(driver)
    url, _, _ = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    assert "inventory" not in driver.current_url
