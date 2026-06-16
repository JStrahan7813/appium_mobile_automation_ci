from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 🎯 MOBILE BLUEPRINT: Using Appium Accessibility IDs (highly stable for Android/iOS)
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "Login button")
        self.error_badge = (AppiumBy.XPATH, "//*[contains(@text, 'do not match')]")

    def enter_credentials(self, username, password):
        """Finds fields and inputs the test strings."""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        """Triggers the tap action on the screen."""
        self.driver.find_element(*self.login_button).click()

    def get_error_message_text(self):
        """Extracts the validation text from the screen."""
        return self.driver.find_element(*self.error_badge).text
