import pytest

from pages.login_page import LoginPage
from utils.logger import create_logger

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