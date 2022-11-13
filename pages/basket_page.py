from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_added_product_name(self):
        assert self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_NAME)
    
    def should_be_added_product_price(self):
        assert self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_PRICE)

    def get_added_product_name(self):
        return self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_NAME).text

    def get_added_product_price(self):
        return self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_PRICE).text

    def there_is_no_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
       "basket_is_not_empty"

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
        "basket_is_not_empty"

    def basket_is_empty_text(self):
         return self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        
    def check_if_basket_is_empty_text(self):
        empty_basket = self.basket_is_empty_text()
        assert empty_basket == 'Your basket is empty. Continue shopping'      

    def basket_is_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
       "basket_is_empty"

        