from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 🎯 STABLE APP NAVIGATION SELECTORS
        self.sidebar_menu_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("menu")')
        self.sidebar_login_item = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log In")')
        
        # 🎯 EXPLICIT DEVELOPER-ASSIGNED FIELD RESOURCE CODES
        # These target the exact text input containers inside the native app layout tree
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "Login button")
        
        # Pulls the error text using standard cross-platform XPath matching
        self.error_badge = (AppiumBy.XPATH, "//*[contains(@text, 'do not match')]")

    def navigate_to_login_screen(self):
        """Clicks the navigation burger menu and jumps to the form screen."""
        self.driver.find_element(*self.sidebar_menu_button).click()
        self.driver.find_element(*self.sidebar_login_item).click()

    def enter_credentials(self, username, password):
        """Finds inputs and populates credential strings."""
        # Clear the placeholder text first if present, then send keys securely
        user_input = self.driver.find_element(*self.username_field)
        user_input.clear()
        user_input.send_keys(username)
        
        pass_input = self.driver.find_element(*self.password_field)
        pass_input.clear()
        pass_input.send_keys(password)

    def click_login(self):
        """Triggers the tap action on the screen button."""
        self.driver.find_element(*self.login_button).click()

    def get_error_message_text(self):
        """Extracts the validation string text from the UI."""
        return self.driver.find_element(*self.error_badge).text
