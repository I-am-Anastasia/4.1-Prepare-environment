from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_URL = (By.CSS_SELECTOR, "[href*='/ru/accounts/login/']")

class ProductPageLocators():
    PRODUCT_URL = (By.CSS_SELECTOR, "[href*='/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear']")
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class*='btn-add-to-basket']")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-6.product_main p")
    PRODUCT_ADDED_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert.success:nth-child(1) div")
    SHIPPING_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert.success:nth-child(2) div")
    PRODUCT_NAME_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert.success:nth-child(1) div")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alertinner strong")


class BasketPageLocators():  
    BASKET_URL = (By.CSS_SELECTOR, "[href*='/ru/basket/']")
    ADDED_PRODUCT_NAME = (By.TAG_NAME, "h3")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-1:nth-child(4) p")