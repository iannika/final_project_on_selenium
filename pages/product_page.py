from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        
    def should_be_correct_name_product(self):
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT).text
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        
        assert alert_name == product_name, "The product card with the price and in the notification does not match"
        
    def should_be_correct_price_product(self):
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_PRODUCT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        
        assert alert_price == product_price, "The product card with the name and in the notification does not match"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but shouldn't be"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The success message does not disappear"