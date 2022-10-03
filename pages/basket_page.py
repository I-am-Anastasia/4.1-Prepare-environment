from .base_page import BasePage
from locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_added_product_name()
        self.should_be_added_product_price()

    def should_be_basket_url(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_URL)

    def should_be_added_product_name(self):
        assert self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_NAME)
    
    def should_be_added_product_price(self):
        assert self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_PRICE)

    def get_added_product_name(self):
        return self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_NAME).text

    def get_added_product_price(self):
        return self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_PRICE).text