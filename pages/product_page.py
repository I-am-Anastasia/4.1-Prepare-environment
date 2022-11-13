from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
        
    def add_product_to_the_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def check_if_product_with_correct_name_added_to_the_basket(self, product_name_on_product_page, product_name_on_basket_page):
        
        assert product_name_on_basket_page == product_name_on_product_page

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_if_product_with_correct_price_added_to_the_basket(self, price1, price2):
    
        assert price1 == price2

    def should_not_be_success_message_for_product(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def product_success_message_is_disappeared_after_product_adding(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE)

    def get_product_name_from_the_meesage(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE)

        




    