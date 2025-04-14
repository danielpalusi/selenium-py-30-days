from pages.login_page import LoginPage
import time
from utils.logger import create_logger

logger = create_logger(__name__)

def test_login(driver, retrieve_config_data):
    logger.info("Starting login test 🚀🚀")

    login_page = LoginPage(driver)

    url, username, password = retrieve_config_data

    login_page.go_to(url)
    login_page.login(username, password)

    assert "inventory" in driver.current_url

    # Simulate: Check for success, ONLY mock test
    success = False
    if success:
        logger.info("Login successful ✅")
    else:
        logger.warning("Login may have failed. UI did not respond as expected ⚠️")

    logger.info("Login test finished ⛳⛳")
    time.sleep(3)