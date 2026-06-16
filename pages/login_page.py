from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 🎯 THE BLUEPRINT: Store all locator strings in one central location
        self.username_field = (By.CSS_SELECTOR, "#user-name")
        self.password_field = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")
        self.error_badge = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_credentials(self, username, password):
        """Reusable action method to fill out the form."""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        """Reusable action method to submit the login form."""
        self.driver.find_element(*self.login_button).click()

    def get_error_message_text(self):
        """Reusable action method to extract warning validation text."""
        return self.driver.find_element(*self.error_badge).text
