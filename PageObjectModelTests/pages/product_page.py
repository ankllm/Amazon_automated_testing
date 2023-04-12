import random
from pages.locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base import Base
from utilities.logger import Logger


class ProductPage(Base):

    def return_price_on_product_page(self):
        price_wh = self.get_element(*ProductPageLocs.product_price_whole_box).text
        price_fr = self.get_element(*ProductPageLocs.product_price_fraction_box).text
        if ',' in price_wh:
            price_wh = self.remove_comma(price_wh)
        price_full = price_wh + '.' + price_fr
        print(f'full price on product page is {price_full}')
        return float(price_full)

    def select_and_return_random_quantity(self):
        print('Trying to select random quantity of product')
        try:
            select_element = self.driver.find_element(*ProductPageLocs.quantity_select)
            select_element.click()
            select_options = self.get_elements(*ProductPageLocs.quantity_option)
            random_option = random.choice(select_options)
            random_option_text = random_option.text
            self.driver.execute_script("arguments[0].scrollIntoView(true);", random_option)
            random_option.click()
            print(f'Selected {random_option_text} products')
            return random_option_text
        except NoSuchElementException:
            print('Cannot select quantity')
            return '1'

    def add_product_price_and_quantity_to_list(self):
        title = self.get_element(*ProductPageLocs.prod_title).text
        print(f'product: {title}')
        price = self.return_price_on_product_page()
        quantity = self.select_and_return_random_quantity()
        print(f'added price: {price}, quantity: {quantity} to list')
        return [price, quantity]

    def add_to_cart(self):
        Logger.add_start_step(method='add_to_cart')
        print('Trying to add product to cart')
        self.get_element(*ProductPageLocs.add_to_cart_button).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(ProductPageLocs.warranty_pane_refuse_button)).click()
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(ProductPageLocs.warranty_pane_close)).click()
            print('warranty pane is closed')
        except TimeoutException:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(AddedToCartLocs.added_to_cart_msg))
        print('product is added to cart')
        Logger.add_end_step(url=self.driver.current_url, method='add_to_cart')

    # def should_be_department_name_on_product_page(self, selected_dep):
    #     dep_name_on_product_page = WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located(*ProductPageLocs.department)).text
    #     self.should_be_equal_texts(dep_name_on_product_page, selected_dep)
    #
    # def should_be_subdep_name_on_product_page(self, selected_subdep):
    #     dep_name_on_product_page = WebDriverWait(self.driver, 5).until(
    #         EC.visibility_of_element_located(*ProductPageLocs.department)).text
    #     self.should_be_equal_texts(dep_name_on_product_page, selected_subdep)
