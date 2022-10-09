import re
from socket import SOCK_DGRAM
import pytest
import time


from pages.product_page import ProductPage
from pages.basket_page import BasketPage

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

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
#urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)

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

@pytest.mark.parametrize('url', urls)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, url):
    page = ProductPage(browser, url)  
    page.open()                   
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_for_product()
      
@pytest.mark.parametrize('url', urls)
def test_guest_cant_see_shipping_success_message_after_adding_product_to_basket(browser, url):
    page = ProductPage(browser, url)  
    page.open()                   
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code() 
    page.should_not_be_success_message_for_shipping()

@pytest.mark.parametrize('url', urls)
def test_guest_cant_see_success_message(browser, url):
    page = ProductPage(browser, url)  
    page.open()                   
    page.should_not_be_success_message_for_product()
    page.should_not_be_success_message_for_shipping()

@pytest.mark.parametrize('link', urls)
def test_product_with_correct_name_for_success_message(browser, link):
    page = ProductPage(browser, link)  
    page.open()                   
    page.add_product_to_the_basket()
    product_name = page.get_product_name()
    product_name_on_the_message = page.get_product_name_from_the_meesage()

    assert product_name == product_name_on_the_message

@pytest.mark.parametrize('link', urls)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)  
    page.open()                   
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code() 
    page.product_success_message_is_disappeared_after_product_adding()

@pytest.mark.parametrize('link', urls)
def test_shipping_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)  
    page.open()                   
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code() 
    page.shipping_success_message_is_disappeared_after_product_adding()

    
    




    

    