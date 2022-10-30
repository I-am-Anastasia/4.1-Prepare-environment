import re
from socket import SOCK_DGRAM
import pytest

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

# def test_guest_can_add_product_to_the_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)  
#     page.open()                   
#     page.add_product_to_the_basket()
#     page.solve_quiz_and_get_code()   

# def test_product_with_correct_name_added_to_the_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)  
#     page.open()                   
#     page.add_product_to_the_basket()
#     page.solve_quiz_and_get_code() 

#     product_name_on_product_page = page.get_product_name()

#     basket_url = "http://selenium1py.pythonanywhere.com/ru/basket/"
#     basket = BasketPage(browser, basket_url)
    
#     basket.open()
#     product_name_on_basket_page = basket.get_added_product_name()

#     assert product_name_on_basket_page == product_name_on_product_page

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
# urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)

# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser, link):   
#     page = ProductPage(browser, link)  
#     page.open()                  
#     page.add_product_to_the_basket()
#     page.solve_quiz_and_get_code()

# @pytest.mark.parametrize('link', urls)
# def test_product_with_correct_price_added_to_the_basket(browser, link):
#     page = ProductPage(browser, link)  
#     page.open()                   
#     page.add_product_to_the_basket()
#     page.solve_quiz_and_get_code() 
    
#     product_price_on_product_page = page.get_product_price()

#     basket_url = "http://selenium1py.pythonanywhere.com/ru/basket/"
#     basket = BasketPage(browser, basket_url)

#     basket.open()
#     product_price_on_basket_page = basket.get_added_product_price()

#     expression = '[\d\s.,]*\d'

#     price1 = re.search(expression, product_price_on_basket_page).group(0)
#     price1 = price1.replace(',', '.')
#     price2 = re.search(expression, product_price_on_product_page).group(0)
   
#     assert price1 == price2

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.get_login_link()

# def test_guest_cannot_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)  
#     page.open()                   
#     page.should_not_be_success_message_for_product()
#     page.should_not_be_success_message_for_shipping()
    
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_basket_link()
#     empty_basket = page.basket_is_empty()
#     assert empty_basket == 'Ваша корзина пуста Продолжить покупки'  

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_the_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)  
        page.open()                   
        page.add_product_to_the_basket()
        page.solve_quiz_and_get_code()   

    def test_user_cannot_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)  
        page.open()                   
        page.should_not_be_success_message_for_product()
        page.should_not_be_success_message_for_shipping()

    




    
    




    

    