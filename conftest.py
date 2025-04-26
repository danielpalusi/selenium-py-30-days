import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.config_parser import config
from utils.logger import create_logger
from utils.screenshot import take_screenshot

def add_headless_option(options, browser_name):
    """
        Add function to add headless option, will be called by create driver function

        Parameter:
        options
        browser_name (string)

        Return value:
        options
        """

    if browser_name == "chrome" or browser_name == "edge":
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    return options

def create_driver(browser_name, headless=False):
    """
    Map the browser based on passed browser name

    Parameter:
    browser_name (string)
    headless (boolean)

    Return value:
    webdriver
    """

    if browser_name == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options = add_headless_option(options, browser_name)
        return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    elif browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options = add_headless_option(options, browser_name)
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not supported yet")

# no need to put @pytest.hookimpl() if there's no parameter added 💡💡
@pytest.hookimpl()
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run with"
    )
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")

@pytest.fixture
def driver(request, browser_name):
    # Setup
    headless = request.config.getoption("--headless")
    driver = create_driver(browser_name, headless)

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

# built-in hook, this will be triggered before and after test
@pytest.hookimpl()
def pytest_runtest_protocol(item, nextitem):
    logger.info(f"Starting test: {item.nodeid} 🚀🚀")

    result = nextitem

    logger.info(f"Test finished: {item.nodeid} ⛳⛳")

    return result

# built-in hook, this will be triggered after test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Before test execution
    outcome = yield

    # After test execution
    report = outcome.get_result()

    if call.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            print("below")
            print(item.nodeid)
            take_screenshot(driver, item.nodeid)