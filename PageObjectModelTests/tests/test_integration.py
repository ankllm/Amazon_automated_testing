from pages.base import Base
from pages.shopping_page import ShoppingPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest


class TestRandomChoice:

    # @pytest.mark.skip
    def test_should_match_prices_on_shopping_and_product_pages(self, driver):
        url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011&ref=nav_em__nav_desktop_sa_intl_monitors_0_2_6_8'
        shop_page = ShoppingPage(driver, url)
        shop_page.open()
        shop_price = shop_page.select_random_product_and_return_its_price()
        prod_page = ProductPage(driver, driver.current_url)
        prod_price = prod_page.return_price_on_product_page()
        prod_page.should_be_equal_texts(shop_price, prod_price)

    @pytest.mark.chrome
    # @pytest.mark.skip
    def test_should_be_correct_number_of_products_in_header_cart(self, driver):
        url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011&ref=nav_em__nav_desktop_sa_intl_monitors_0_2_6_8'
        shop_page = ShoppingPage(driver, url)
        shop_page.open()
        count = 0
        for _ in range(2):
            shop_page.open_random_product_in_new_tab_and_switch()
            prod_page = ProductPage(driver, driver.current_url)
            qty = prod_page.select_and_return_random_quantity()
            prod_page.add_to_cart()
            count += int(qty)
            prod_page.should_be_correct_number_of_products_in_header_cart(str(count))
            prod_page.close_current_window_and_switch_to_initial(0)

    # The method adds random products' prices and quantities to list, calculates total quantity and subtotal price of
    # added products and compares the corresponding values on cart page
    @pytest.mark.chrome
    # @pytest.mark.skip
    def test_should_be_correct_subtotal_and_quantity_in_cart_create_list(self, driver):
        url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011&ref=nav_em__nav_desktop_sa_intl_monitors_0_2_6_8'
        shop_page = ShoppingPage(driver, url)
        shop_page.open()
        price_quantity_list = []
        prod_nums = shop_page.return_random_products_nums(3)
        for num in prod_nums:
            shop_page.open_product_in_new_tab_by_its_num_and_switch(num)
            prod_page = ProductPage(driver, driver.current_url)
            price_quantity_list.append(prod_page.add_product_price_and_quantity_to_list())
            prod_page.add_to_cart()
            prod_page.close_current_window_and_switch_to_initial(0)
        calc_subtotal = shop_page.calculate_and_return_subtotal_in_list(price_quantity_list)
        calc_qty = shop_page.calculate_and_return_prod_quantity_in_list(price_quantity_list)
        shop_page.open_cart()
        cart_page = CartPage(driver, driver.current_url)
        cart_page.should_be_correct_subtotal(calc_subtotal)
        cart_page.should_be_correct_items_number_in_buybox_list(calc_qty)


class TestCertainChoice:

    # @pytest.mark.skip
    def test_should_be_subdeparment_name_on_shopping_page(self, driver):
        url = 'https://www.amazon.com/'
        driver.maximize_window()
        base_page = Base(driver, url)
        base_page.open()
        base_page.open_menu()
        base_page.see_all_departments()
        base_page.select_department_by_its_number(6)
        subdep_name = base_page.select_and_return_subdep_by_its_number(6, 7)
        shop_page = ShoppingPage(driver, driver.current_url)
        shop_page.should_be_subdep_name_on_shopping_page(subdep_name)
