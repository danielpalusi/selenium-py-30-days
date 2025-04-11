from pages.login_page import LoginPage
import time
from utils.config_parser import config
from utils.logger import create_logger

logger = create_logger(__name__)

def test_login(driver):
    logger.info("Starting login test 🚀🚀")
    print(f"Logger name is: {__name__}")

    login_page = LoginPage(driver)

    # return is dict, so we can easily access it
    # dict like object in js
    url = config['base_url']
    username = config['username']
    password = config['password']

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