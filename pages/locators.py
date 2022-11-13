from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_URL = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM_FIELD = (By.ID, "id_registration-password2")
    SIGN_UP_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class*='btn-add-to-basket']")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-6.product_main p")
    PRODUCT_ADDED_SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div")
    PRODUCT_NAME_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert.success:nth-child(1) div")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alertinner strong")

class BasketPageLocators():  
    ADDED_PRODUCT_NAME = (By.TAG_NAME, "h3")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-1:nth-child(4) p")
    EMPTY_BASKET = (By.CSS_SELECTOR,"#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_ITEMS = (By.CSS_SELECTOR, "[class*='basket-items']")