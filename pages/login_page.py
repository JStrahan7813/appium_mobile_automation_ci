from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 🎯 NAVIGATION TARGETS
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
        """Intercepts both native Android System Dialog Alerts and on-screen text overlays."""
        try:
            # ⏳ Look for a native Android UI Alert popup box context first (Max 5s wait)
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"⚠️ Native Android Dialog Alert Intercepted: '{alert_text}'")
            alert.accept() # Dismiss the pop-up modal so the session cleans up cleanly
            return alert_text
        except:
            # 🔄 Fallback: If no system dialog modal box popped up, scrape the screen elements directly
            print("🔍 No native dialog box found, scraping screen text layers instead...")
            fallback_badge = (AppiumBy.XPATH, "//*[contains(@text, '')]")
            elements = self.driver.find_elements(*fallback_badge)
            for el in elements:
                text_val = el.text
                if any(word in text_val.lower() for word in ["credential", "incorrect", "match", "password", "user"]):
                    return text_val
            return ""
