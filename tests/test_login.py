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
    
    # Configure explicit modern W3C capabilities using standard options structure
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.set_capability("appium:app", "https://github.com/saucelabs/my-demo-app-android/releases/download/v1.0.13/mda-1.0.13-15.apk")
    
    # 🎯 FORCE EXPLICIT APPIUM 2 COMPLIANCE BY TARGETING FIXED ANDROID VERSIONS
    options.set_capability("appium:deviceName", "Samsung Galaxy.*")
    options.set_capability("appium:platformVersion", "13") # Restricts to a stable version to bypass protocol strictness
    
    options.set_capability("sauce:options", {
        "name": "Appium Real Device Mobile Portfolio Run",
        "build": "Build-2.0"
    })

    driver = webdriver.Remote(sauce_url, options=options)
    yield driver
    driver.quit()
