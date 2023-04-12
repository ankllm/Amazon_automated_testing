from pages.base import Base
from pages.shopping_page import ShoppingPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignIn
import pytest


class TestRandomChoice:

    @pytest.mark.chrome
    # @pytest.mark.skip
    def test_buy_product_through_menu_selection(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.open_menu()
        base_page.see_all_departments()
        base_page.select_and_return_random_subdep(base_page.select_and_return_random_department_number())
        shop_page = ShoppingPage(driver, driver.current_url)
        shop_page.select_random_product()
        prod_page = ProductPage(driver, driver.current_url)
        prod_page.open()
        prod_list = []
        prod_list.append(prod_page.add_product_price_and_quantity_to_list())
        prod_page.add_to_cart()
        prod_page.open_cart()
        cart_page = CartPage(driver, driver.current_url)
        cart_page.should_be_products_in_cart(prod_list)
        cart_page.click_on_proceed_to_checkout()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.should_be_signin_form()







