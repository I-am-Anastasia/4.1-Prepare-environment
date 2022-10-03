from .base_page import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.add_product_to_the_basket()
        self.should_be_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()
        self.get_product_name()
        self.get_product_price()
        
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


    