from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_NAME_PRODUCT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)')
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".alert:nth-child(1) a")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a.btn")
    
    
class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items>.row")
    