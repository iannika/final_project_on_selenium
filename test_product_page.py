import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.login_test
class TestUserAddToBasketFromProductPage():
  @pytest.fixture(scope="function", autouse=True)
  def setup(self, browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    self.login_page = LoginPage(browser, link)
    self.login_page.open()
    email_rnd = str(time.time()) + "@fakemail.org"
    password_rnd = str(time.time())
    self.login_page.register_new_user(email=email_rnd, password=password_rnd)
    self.login_page.should_be_authorized_user()

     
  def test_user_cant_see_success_message(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
  
  def test_user_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_be_correct_name_product()
    page.should_be_correct_price_product()
  
  

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
  current_link = link
  page = ProductPage(browser, current_link)
  page.open()
  page.should_be_add_to_basket()
  page.solve_quiz_and_get_code()
  page.should_be_correct_name_product()
  page.should_be_correct_price_product()
  time.sleep(5)

@pytest.mark.xfail     
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  page = ProductPage(browser, link)
  page.open()
  page.should_be_add_to_basket()
  page.should_not_be_success_message()
  
def test_guest_cant_see_success_message(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  page = ProductPage(browser, link)
  page.open()
  page.should_not_be_success_message()

@pytest.mark.xfail   
def test_message_disappeared_after_adding_product_to_basket(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  page = ProductPage(browser, link)
  page.open()
  page.should_be_add_to_basket()
  page.should_is_disappeared_success_message()
  
def test_guest_should_se_login_link_on_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(browser, link)
  page.open()
  page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(browser, link)
  page.open()
  page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = BasketPage(browser, link)
  page.open()
  page.should_go_to_basket_page()
  page.should_not_be_products_in_basket()
  page.should_be_presented_message_about_empty_basket()
