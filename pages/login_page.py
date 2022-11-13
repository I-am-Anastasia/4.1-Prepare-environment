from .base_page import BasePage
from .locators import LoginPageLocators 

class LoginPage(BasePage):
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD)
        confirm_password_field.click()
        confirm_password_field.send_keys(password)
        sign_up_button = self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON)
        sign_up_button.click()