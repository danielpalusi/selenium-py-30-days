import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    """
    Provide screenshot by capture the page, and store it in screenshot dir, image is stored using
    png file extension

    Parameter:
    driver
    name (text)

    No return
    """
    os.makedirs("screenshot", exist_ok=True)

    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot/{name}_{time}.png"

    driver.save_screenshot(file_name)
    print("Screenshot is saved")
