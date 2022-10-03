import time

from pages.product_page import ProductPage
from pages.basket_page import BasketPage

 def test_guest_can_add_product_to_the_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
     page = ProductPage(browser, link)  
     page.open()                   
     page.add_product_to_the_basket()
     page.solve_quiz_and_get_code()   

def test_product_with_correct_name_added_to_the_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  
    page.open()                   
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code() 

    product_name_on_product_page = page.get_product_name()

    basket_url = "http://selenium1py.pythonanywhere.com/ru/basket/"
    basket = BasketPage(browser, basket_url)
    
    basket.open()
    product_name_on_basket_page = basket.get_added_product_name()

    assert product_name_on_basket_page == product_name_on_product_page

def test_product_with_correct_price_added_to_the_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  
    page.open()                   
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code() 

    product_price_on_product_page = page.get_product_price()

    basket_url = "http://selenium1py.pythonanywhere.com/ru/basket/"
    basket = BasketPage(browser, basket_url)
    basket.open()
    product_price_on_basket_page = basket.get_added_product_price()

    assert product_price_on_basket_page == product_price_on_product_page
    

