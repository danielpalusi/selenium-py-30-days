from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_visibility(driver, locator, timeout=10):
    return WebDriverWait(driver,timeout).until(EC.visibility_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_for_presence(driver, locator, timeout=10):
    return  WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))