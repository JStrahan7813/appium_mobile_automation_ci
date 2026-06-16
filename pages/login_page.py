from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 🎯 BULLETPROOF NAVIGATION SELECTORS
        self.sidebar_menu_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("menu")')
        self.sidebar_login_item = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log In")')
        
        # 🎯 STRICT INPUT FIELD SELECTORS (Targets ONLY the editable text boxes)
        self.username_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").descriptionContains("Username")')
        self.password_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").descriptionContains("Password")')
        self.login_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Login")')
        self.error_badge = (AppiumBy.XPATH, "//*[contains(@text, 'do not match')]")

    def navigate_to_login_screen(self):
        """Clicks the navigation burger menu and jumps to the form screen."""
        self.driver.find_element(*self.sidebar_menu_button).click()
        self.driver.find_element(*self.sidebar_login_item).click()

    def enter_credentials(self, username, password):
        """Finds inputs and populates credential strings."""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        """Triggers the tap action on the screen button."""
        self.driver.find_element(*self.login_button).click()

    def get_error_message_text(self):
        """Extracts the validation string text from the UI."""
        return self.driver.find_element(*self.error_badge).text
