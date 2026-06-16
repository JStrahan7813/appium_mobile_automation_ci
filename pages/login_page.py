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
        
        # 🎯 CLICKABLE ACTION TARGET
        self.login_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().clickable(true).descriptionContains("Login")')

    def navigate_to_login_screen(self):
        """Clicks the navigation burger menu and jumps to the form screen."""
        self.driver.find_element(*self.sidebar_menu_button).click()
        self.driver.find_element(*self.sidebar_login_item).click()

    def enter_credentials(self, username, password):
        """Finds inputs and populates credential strings cleanly."""
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
        """Intercepts the error notification directly from the Android layout view tree."""
        # ⏳ Give the UI warning container 5 seconds to animate and settle on screen
        WebDriverWait(self.driver, 5)
        
        # 🎯 Dynamic layout scrape: find any text component containing security warning keywords
        error_selector = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i).*(credentials|incorrect|match|password|user).*")')
        try:
            element = self.driver.find_element(*error_selector)
            # Pull the display string using the native get_attribute call for complete reliability
            text_found = element.get_attribute("text") or element.text
            print(f"🔍 Automation found validation text: '{text_found}'")
            return text_found
        except:
            print("⚠️ Direct selector missed, performing universal fallback string extraction...")
            all_text_elements = self.driver.find_elements(AppiumBy.XPATH, "//*[@text!='']")
            for el in all_text_elements:
                val = el.get_attribute("text")
                if any(word in val.lower() for word in ["credential", "incorrect", "match", "password"]):
                    return val
            return ""
