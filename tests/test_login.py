import pytest
from appium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="function")
def driver():
    print("\n🚀 Initializing highly stable headless browser testing environment...")
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=375,812") # Mobile dimensions
    
    # Target the responsive web layout matching the mobile app structure
    driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=chrome_options)
    yield driver
    driver.quit()

def test_invalid_login_error_message(driver):
    """Validates that entering wrong credentials triggers the correct warning badge."""
    # Navigate to the official SauceLabs practice responsive dashboard web app
    driver.get("https://www.saucedemo.com/")
    
    print("🔍 Executing functional UI assertion selectors...")
    
    # 1. Use universal CSS selectors (The '#' symbol targets IDs perfectly in web engines)
    driver.find_element(by="css selector", value="#user-name").send_keys("wrong_user")
    driver.find_element(by="css selector", value="#password").send_keys("wrong_password")
    
    # 2. Fire the login sequence button action
    driver.find_element(by="css selector", value="#login-button").click()

    # 3. Assert the targeted UI error message badge renders perfectly
    error_text = driver.find_element(by="css selector", value="h3[data-test='error']").text
    assert "do not match" in error_text.lower()
    print("✅ Success! Responsive layout verification complete.")
