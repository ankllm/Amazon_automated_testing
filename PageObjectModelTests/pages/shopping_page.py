import random
import time
from pages.locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from utilities.logger import Logger


class ShoppingPage(Base):

    # The method collects all products given on page 1 and selects one of them
    def select_random_product(self):
        prods = self.get_elements(*ShoppingPageProductsLocs.available_product)
        p = random.choice(prods)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", p)
        p.click()
        print('Selected random product')

    def select_price_filter(self, method, locator):
        f = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((method, locator)))
        f.click()

    def get_full_price_of_all_products(self):
        whs = self.get_elements(*ShoppingPageProductsLocs.price_whole)
        whs_text = self.get_elements_text(whs)
        frs = self.get_elements(*ShoppingPageProductsLocs.price_fraction)
        frs_text = self.get_elements_text(frs)
        for i in range(len(whs)):
            whs_text[i] += f'.{frs_text[i]}'
            whs_text[i] = float(whs_text[i])
        return whs_text

    def should_be_correct_prices_on_shopping_page(self, mn, mx):
        print(f'Checking {mn}-{mx} price filter')
        prices = self.get_full_price_of_all_products()
        for price in prices:
            if mn <= price < mx:
                print(f'\033[32m{price}\033[0m')
            else:
                print(f'\033[31m{price}\033[0m')
        print('Price filter check complete')

    def return_random_products_nums(self, prod_quantity):
        elems = self.get_elements(*ShoppingPageProductsLocs.available_product)
        prod_nums = random.sample(range(1, len(elems) + 1), prod_quantity)
        return prod_nums

    def open_product_in_new_tab_by_its_num_and_switch(self, prod_num):
        prod = self.get_element(By.XPATH, f'//*[contains(text(), "Ships to")]/ancestor::*[@data-component-type]//*[@data-component-type="s-search-result"][{prod_num}]')
        last_window = len(self.driver.window_handles) - 1
        self.open_in_new_tab(prod)
        self.driver.switch_to.window(self.driver.window_handles[last_window+1])
        print('Opened the product in a new tab')

    def open_random_product_in_new_tab_and_switch(self):
        prods = self.get_elements(*ShoppingPageProductsLocs.available_prod_image)
        prod = self.get_random_element(prods)
        last_window = len(self.driver.window_handles) - 1
        self.open_in_new_tab(prod)
        self.driver.switch_to.window(self.driver.window_handles[last_window+1])
        print('Opened some random product in a new tab')

    def return_brands_names(self):
        brands_list = self.get_elements(By.XPATH, '//li[contains(@id, "p_89/")]//a')
        brands_names_list = self.get_elements_text(brands_list)
        return brands_names_list

    def return_products_titles(self):
        titles = self.get_elements(*ShoppingPageProductsLocs.product_title)
        titles_text = self.get_elements_text(titles)
        return titles_text

    def select_brand_by_name(self, name):
        self.get_element(By.XPATH, f'//div[@id="brandsRefinements"]//span[text()="{name}"]').click()

    def should_be_brand_name_in_prod_title(self, brand_name):
        print(f'Checking that "{brand_name}" is in product titles')
        titles_list = self.return_products_titles()
        for title in titles_list:
            try:
                assert brand_name in title
            except AssertionError:
                try:
                    assert brand_name.lower() in title.lower()
                except AssertionError:
                    print('\033[31mProduct title does not contain brand name\033[0m')
                print('\033[32mProduct title contains brand name but the cases are different:\033[0m')
                print(f'   -brand: {brand_name}; title: {title}')
        print(f'"{brand_name}" brand check complete')

    def check_brand_filter(self):
        Logger.add_start_step(method='check_brand_filter')
        print('Testing brand filters')
        brands_names_list = self.return_brands_names()
        for brand_name in brands_names_list:
            print(f'Selecting "{brand_name}"')
            self.select_brand_by_name(brand_name)
            self.should_be_brand_name_in_prod_title(brand_name)
            print(f'Deselecting "{brand_name}"')
            self.select_brand_by_name(brand_name)
        print('Brand filters testing complete')
        Logger.add_end_step(url=self.driver.current_url, method='check_brand_filter')

    def select_random_product_and_return_its_price(self):
        elems = self.get_elements(*ShoppingPageProductsLocs.available_product)
        prod_num = random.choice(range(1, len(elems) + 1))
        prod = self.get_element(By.XPATH, f'//div[@data-component-type="s-search-result"][{prod_num}]')
        price_wh = self.get_element(
            By.XPATH, f'//div[@data-component-type="s-search-result"][{prod_num}]//span[@class="a-price-whole"]').text
        price_fr = self.get_element(
            By.XPATH, f'//div[@data-component-type="s-search-result"][{prod_num}]//span[@class="a-price-fraction"]').text
        time.sleep(1)
        prod.click()
        price_full = f'{price_wh}.{price_fr}'
        print(f'full price on shopping page is {price_full}')
        return float(price_full)

    def should_be_subdep_name_on_shopping_page(self, subdep_name):
        print(f'Checking that the selected subdepartment "{subdep_name}" is on shopping page ')
        self.is_element_present(By.XPATH, f'//div[@id="departments"]//*[text()="{subdep_name}"]')

    # def select_certain_brand(self, brand):
    #     brand = self.get_element(By.XPATH, f'//span[text()="Brand"]/parent::div/following-sibling::ul/descendant::span[text()="{brand}"]')
    #     brand.click()
    #     print(f'Selected "{brand}"')
    #
    # def select_and_return_random_brand(self):
    #     brands_list = self.get_elements((By.XPATH, *ShoppingPageFilterLocs.brand_new))
    #     brand = random.choice(brands_list)
    #     brand_name = brand.text
    #     brand.click()
    #     print(f'Selected "{brand_name}"')
    #     return brand_name

    # def select_and_return_random_brand_old(self):
    #     brands_list = self.get_elements(*ShoppingPageFilterLocs.brand_old)
    #     brand = random.choice(brands_list)
    #     name = brand.get_attribute("aria-label")
    #     brand.click()
    #     return name

    # def choose_random_price_filter(self):
    #     fs = self.get_elements((By.XPATH,  '//li[contains(@id,"p_36/125350")]'))
    #     f = random.choice(fs)
    #     f.click()

    # def input_min_price(self, price):
    #     elem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(*ShoppingPageFilterLocs.price_filter_range_min))
    #     elem.send_keys(price)
    #
    # def input_max_price(self, price):
    #     elem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(*ShoppingPageFilterLocs.price_filter_range_max))
    #     elem.send_keys(price)
    #
    # def apply_input_prices(self):
    #     elem = WebDriverWait(self.driver, 2).until(
    #         EC.element_to_be_clickable(*ShoppingPageFilterLocs.price_filter_range_go))
    #     elem.click()
