import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage
import time

@pytest.fixture(scope="function")
def driver():
    # Fetch credentials securely out of GitHub Actions environment variables
    sauce_username = os.environ.get("SAUCE_USERNAME")
    sauce_access_key = os.environ.get("SAUCE_ACCESS_KEY")
    
    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    
    print("\n📱 Initializing modern Appium session on Sauce Labs RDC...")
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    
    # Securely matches the app binary layout uploaded via curl in your yaml file
    options.set_capability("appium:app", "storage:filename=mda-2.2.0-25.apk")
    
    options.set_capability("sauce:options", {
        "name": "Appium Real Device Mobile Portfolio Run",
        "build": "Build-8.0",
        "appiumVersion": "latest"
    })

    driver = webdriver.Remote(sauce_url, options=options)
    yield driver
    driver.quit()


# 🎯 THE ACTUAL TEST AUTOMATION RUNS HERE
def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge."""
    print("🚀 Test script executing live on Sauce Labs physical device...")
    
    # Connect the driver instance to our Page Object layout structure
    login_page = LoginPage(driver)
    
    # 📱 Step 1: Wait 3 seconds to let the mobile application draw smoothly on the screen
    time.sleep(3)
    
    # 📱 Step 2: Leverage our Page Object methods to type details into the app inputs
    print("✍️ Typing invalid credentials...")
    login_page.enter_credentials("wrong_user@example.com", "bad_password")
    
    # 📱 Step 3: Trigger the touch tap execution command on the login submit link
    print("🖱️ Clicking login button...")
    login_page.click_login()
    
    # 📱 Step 4: Extract the system error text and make sure it behaves correctly
    time.sleep(1)
    error_text = login_page.get_error_message_text()
    print(f"🔍 Found error message on screen: '{error_text}'")
    
    # This checks that the specific validation string shows up in the user interface
    assert "Provided credentials do not match any user in this service" in error_text
    print("✅ Assert passed! The invalid login error message is correct.")
