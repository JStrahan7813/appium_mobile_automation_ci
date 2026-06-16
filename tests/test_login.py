import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage 

@pytest.fixture(scope="function")
def driver():
    # Fetch your secure credentials straight out of the environment
    sauce_username = os.environ.get("SAUCE_USERNAME")
    sauce_access_key = os.environ.get("SAUCE_ACCESS_KEY")
    
    # Target the global Sauce Labs real device cloud endpoint
    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    
    print("\n📱 Initializing remote real-device Appium session on Sauce Labs...")
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    
    # 🎯 CLOUD EXCLUSIVE CAPABILITIES
    options.set_capability("appium:deviceName", "Samsung Galaxy.*") # Dynamically requests any real Samsung phone
    options.set_capability("appium:app", "storage:filename=mda-1.0.13-15.apk") # Targets Sauce's native demo app
    options.set_capability("sauce:options", {
        "name": "Appium Real Device Mobile Portfolio Run",
        "build": "Build-1.0"
    })

    driver = webdriver.Remote(sauce_url, options=options)
    yield driver
    driver.quit()

def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge on a real device."""
    login_page = LoginPage(driver)
    
    print("🔍 Interacting with native app elements via POM on a live phone...")
    
    # Since we are back on a native mobile app, your POM page file class 
    # needs to use mobile locator strategies (like By.ACCESSIBILITY_ID or By.XPATH)
    # instead of the web "#user-name" CSS strings we used for Chrome.
