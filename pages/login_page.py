from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 🎯 APP NAVIGATION SELECTORS
        self.sidebar_menu_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("menu")')
        self.sidebar_login_item = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log In")')
        
        # 🎯 FALLBACK STRUCTURAL INDEXING FOR INPUTS
        self.username_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
        self.password_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
        
        # 🎯 BULLETPROOF BUTTON SELECTOR
        self.login_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().clickable(true).descriptionContains("Login")')
        
        # 🎯 Broad, flexible XPath matching for any error text elements that show up on screen
        self.error_badge = (AppiumBy.XPATH, "//*[contains(@text, 'credentials') or contains(@text, 'Incorrect') or contains(@text, 'not match')]")

    def navigate_to_login_screen(self):
        """Clicks the navigation burger menu and jumps to the form screen."""
        self.driver.find_element(*self.sidebar_menu_button).click()
        self.driver.find_element(*self.sidebar_login_item).click()

    def enter_credentials(self, username, password):
        """Finds inputs and populates credential strings."""
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
        """Safely waits for the error element to appear on the UI before grabbing text."""
        # ⏳ Dynamic 10-second explicit wait to catch the pop-up animation perfectly
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_id_located(self.error_badge) if False else EC.visibility_of_element_located(self.error_badge))
        return element.text
