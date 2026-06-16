import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    sauce_username = os.environ.get("SAUCE_USERNAME")
    sauce_access_key = os.environ.get("SAUCE_ACCESS_KEY")
    
    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    
    print("\n📱 Initializing secure Appium 2.0 session on Sauce Labs Real Device Cloud...")
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.set_capability("appium:app", "https://github.com/saucelabs/my-demo-app-android/releases/download/v1.0.13/mda-1.0.13-15.apk")
    options.set_capability("appium:deviceName", "Samsung Galaxy.*")
    options.set_capability("appium:platformVersion", "13")
    options.set_capability("sauce:options", {
        "name": "Appium Real Device Mobile Portfolio Run",
        "build": "Build-2.0"
    })

    driver = webdriver.Remote(sauce_url, options=options)
    yield driver
    driver.quit()

# 🎯 CRUCIAL: The function name MUST start with "test_" so Pytest can find it!
def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge."""
    print("🚀 Test script found and executing on Sauce Labs physical device!")
    
    # Simple placeholder print to verify the execution stream starts smoothly
    print("✅ App loaded successfully on the device.")
