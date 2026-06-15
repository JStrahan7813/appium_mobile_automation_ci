import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    # Define modern Appium 2.0 Options instead of old deprecated capabilities dicts
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    options.app = "./app-release.apk"  # Relative path where CI downloads the APK
    options.auto_grant_permissions = True

    # Connect to the local Appium Server running on the runner
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge."""
    # 1. Click the Menu hamburger icon via accessibility id
    menu = driver.find_element(by="accessibility id", value="open menu")
    menu.click()

    # 2. Click the Login menu item via native text matching
    login_menu_item = driver.find_element(by="xpath", value="//android.widget.TextView[@text='Log In']")
    login_menu_item.click()

    # 3. Enter test credentials into the interactive elements
    driver.find_element(by="accessibility id", value="Username input field").send_keys("wrong_user")
    driver.find_element(by="accessibility id", value="Password input field").send_keys("wrong_password")
    driver.find_element(by="accessibility id", value="Login button").click()

    # 4. Assert that the error text string renders as expected
    error_text = driver.find_element(by="xpath", value="//android.widget.TextView[@text='Provided credentials do not match any user in this service.']").text
    assert "do not match" in error_text
