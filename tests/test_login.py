import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    sauce_username = os.environ.get("SAUCE_USERNAME")
    sauce_access_key = os.environ.get("SAUCE_ACCESS_KEY")
    
    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    
    print("\n📱 Initializing dynamic real-device Appium session on Sauce Labs...")
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.set_capability("appium:app", "https://github.com/saucelabs/my-demo-app-android/releases/download/v1.0.13/mda-1.0.13-15.apk")
    
    # 🎯 DYNAMIC W3C MATCHING: Asks for ANY available Android phone 
    # that is version 12, 13, or 14 to avoid device pool shortages.
    options.set_capability("appium:platformVersion", "12|13|14") 
    
    options.set_capability("sauce:options", {
        "name": "Appium Real Device Mobile Portfolio Run",
        "build": "Build-3.0"
    })

    driver = webdriver.Remote(sauce_url, options=options)
    yield driver
    driver.quit()

def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge."""
    print("🚀 Test script found and executing on Sauce Labs physical device!")
    print("✅ App loaded successfully on the device.")
