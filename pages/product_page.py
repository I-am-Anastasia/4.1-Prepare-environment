from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
        
    def add_product_to_the_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_product_url(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_URL)

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON)

    def should_be_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message_for_product(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_not_be_success_message_for_shipping(self):
        assert self.is_not_element_present(*ProductPageLocators.SHIPPING_SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def product_success_message_is_disappeared_after_product_adding(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE)

    def shipping_success_message_is_disappeared_after_product_adding(self):
        assert self.is_disappeared(*ProductPageLocators.SHIPPING_SUCCESS_MESSAGE)

    def get_product_name_from_the_meesage(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE)

    def get_login_link(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_URL)
        login_link.click()

        




    