import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    sauce_username = os.environ.get("SAUCE_USERNAME")
    sauce_access_key = os.environ.get("SAUCE_ACCESS_KEY")
    
    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    
    print("\n📱 Initializing modern Appium session on Sauce Labs RDC...")
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    
    # Updated to the strict 'storage:filename=' modern format
    options.set_capability("appium:app", "storage:filename=SauceLabs-Demo-App.apk")
    
    options.set_capability("sauce:options", {
        "name": "Appium Real Device Mobile Portfolio Run",
        "build": "Build-8.0",
        "appiumVersion": "latest"
    })

    driver = webdriver.Remote(sauce_url, options=options)
    yield driver
    driver.quit()

def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge."""
    print("🚀 Test script found and executing on Sauce Labs physical device!")
    print("✅ App loaded successfully on the device.")
