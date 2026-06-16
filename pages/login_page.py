from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.sidebar_menu_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("menu")')
        self.sidebar_login_item = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log In")')
        
        self.username_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
        self.password_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
        
        self.login_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().clickable(true).descriptionContains("Login")')
        self.error_badge = (AppiumBy.XPATH, "//*[contains(@text, 'match') or contains(@text, 'Incorrect') or contains(@text, 'credential')]")

    def navigate_to_login_screen(self):
        self.driver.find_element(*self.sidebar_menu_button).click()
        self.driver.find_element(*self.sidebar_login_item).click()

    def enter_credentials(self, username, password):
        user_input = self.driver.find_element(*self.username_field)
        user_input.clear()
        user_input.send_keys(username)
        
        pass_input = self.driver.find_element(*self.password_field)
        pass_input.clear()
        pass_input.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message_text(self):
        try:
            return self.driver.find_element(*self.error_badge).text
        except:
            return ""
