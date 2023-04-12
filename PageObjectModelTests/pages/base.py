import datetime
import random
import time
from selenium.webdriver import Keys

from utilities.logger import Logger
from .locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class Base:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, method, locator):
        try:
            WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            print('\033[31mElement is not present\033[0m')
            return False
        print('\033[32mElement is present\033[0m')
        return True

    def is_element_not_present(self, method, locator):
        try:
            WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            print('\033[32mElement is not present\033[0m')
            return True
        print('\033[31mElement is  present\033[0m')
        return False

    def is_element_visible(self, method, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((method, locator)))
        except TimeoutException:
            print('\033[31mElement is not visible\033[0m')
            return False
        print('\033[32mElement is visible\033[0m')
        return True

    def is_element_invisible(self, method, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((method, locator)))
        except TimeoutException:
            print('\033[31mElement is visible\033[0m')
            return False
        print('\033[32mElement is not visible\033[0m')
        return True

    def open_in_new_tab(self, elem):
        action = ActionChains(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        windows = self.driver.window_handles
        action.key_down(Keys.CONTROL).click(on_element=elem).key_up(Keys.CONTROL).perform()
        WebDriverWait(self.driver, 12).until(EC.new_window_is_opened(windows))

    def close_current_window_and_switch_to_initial(self, initial_window_index):
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[initial_window_index])

    def remove_focus(self, element):
        element.send_keys(Keys.TAB)

    def get_element(self, method, locator):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((method, locator)))
        return elem

    def get_elements(self, method, locator):
        elements = WebDriverWait(self.driver, 7).until(EC.visibility_of_any_elements_located((method, locator)))
        return elements

    def get_random_element(self, elements):
        element = random.choice(elements)
        return element

    def get_elements_attributes(self, elements, attribute):
        attributes = []
        for elem in elements:
            attributes.append(elem.get_attribute(attribute))
        return attributes

    def get_elements_text(self, elements):
        l_text = []
        for elem in elements:
            l_text.append(elem.text)
        return l_text

    def make_price_from_str(self, price):
        p = ''
        for i in price:
            if i in '1234567890.':
                p += i
        return float(p)

    def should_be_substring_in_text(self, substring, text):
        try:
            assert substring in text
            print(f'\033[32m"{substring}" in "{text}" \033[0m')
        except AssertionError:
            print(f'\033[31m"{text}" does not contain "{substring}" \033[0m')

    def should_be_equal_texts(self, text1, text2):
        try:
            assert text1 == text2
            print(f'\033[32m"{text1}" is equal to "{text2}" \033[0m')
        except AssertionError:
            print(f'\033[31m"{text1}" is not equal to "{text2}" \033[0m')

    def should_be_sign_in_button_in_header(self):
        print('Trying to find sign in button in header')
        self.is_element_present(*HeaderLocs.sign_in)
        time.sleep(2)

    def click_on_sign_in_button(self):
        self.get_element(*HeaderLocs.sign_in).click()

    def open_menu(self):
        menu = self.driver.find_element(*MenuLocs.menu_button)
        menu.click()

    def see_all_departments(self):
        all_departments = self.get_element(*MenuLocs.see_all_departments)
        all_departments.click()

    # The list of departments number can be found in locators.py
    def select_department_by_its_number(self, dep_number):
        department = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f'//a[@data-menu-id="{dep_number}"]')))
        department.click()

    # The department number is used to select any of subdepartments that belong to the department
    def select_and_return_random_department_number(self):
        n = random.choice(departments_numbers_for_random_choice_tests)
        dep = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, f'//a[@data-menu-id="{n}"]')))
        dep.click()
        return n

    # This is a universal method. You can either save the returned number in a variable to for further checks or use
    # the method only to select a subdepartment
    def select_and_return_subdep_by_its_number(self, dep_num, subdep_num):
        subdep = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, f'//*[@data-menu-id="{dep_num}"]/li[{subdep_num}]/a[@class="hmenu-item"]')))
        subdep_name = subdep.text
        subdep.click()
        return subdep_name

    def select_and_return_random_subdep(self, dep_number):
        subdeps = WebDriverWait(self.driver, 7).until(EC.presence_of_all_elements_located((By.XPATH, f'//ul[@data-menu-id="{dep_number}"]//a[@class="hmenu-item"]')))
        subdep = self.get_random_element(subdeps)
        subdep_name = subdep.text
        subdep.click()
        return subdep_name

    # The element with the button leading back to main menu contains the number of selected department
    def back_to_menu_from_department_by_its_number(self, number):
        element = self.driver.find_element(By.XPATH, f'//a[@data-ref-tag ="nav_em_1_{number}_BT_0_main_menu"]')
        element.click()

    # This method successively selects all departments in main menu, makes sure that this action has the right effect,
    # clicks on go back button and checks that main menu is visible
    def select_department_and_go_back(self):
        Logger.add_start_step(method='select_department_and_go_back')
        print('Checking department selection')
        for i in departments_numbers :
            dep = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f'//a[@data-menu-id="{i}"]')))
            name = dep.text
            dep.click()
            print(f'Selected {name} department, trying to find it in the opened list of subdepartments')
            time.sleep(1)
            self.is_element_visible(By.XPATH, f'//div[contains(text(),"{name.lower()}") and @class="hmenu-item hmenu-title "]')
            self.back_to_menu_from_department_by_its_number(i)
            print('Got back, making sure that the menu is visible')
            time.sleep(1)
            self.is_element_visible(*MenuLocs.menu)
        Logger.add_end_step(url=self.driver.current_url, method='select_department_and_go_back')

    def return_items_quantity_in_header_cart(self):
        return self.get_element(*HeaderLocs.cart_products_number).text

    def open_cart(self):
        cart_element = self.get_element(*HeaderLocs.cart)
        cart_element.click()

    # The method receives a number, which you can get summing the number of products you add to cart, and compares it
    # to the number of products given in cart in header
    def should_be_correct_number_of_products_in_header_cart(self, number):
        if 'cart' not in self.driver.current_url:
            self.driver.refresh()
        products_number = self.get_element(*HeaderLocs.cart_products_number).text
        print(f'Product quantity of added products: {number}')
        print(f'Product quantity in header cart: {products_number}')
        try:
            self.get_element(By.XPATH, f'//span[@id="nav-cart-count" and text()="{number}"]')
        except NoSuchElementException:
            print(f'\033[31mProducts number in the header cart ({products_number}) and the number of products added ({number}) do not coincide\033[0m')

    # This method receives a list of products (their prices and quantities) and calculates subtotal price.
    # The list can be created with the method 'add_product_price_and_quantity_to_list()' from ProductPage class
    def calculate_and_return_subtotal_in_list(self, prices_and_qty_list):
        subtotal = 0
        for i in range(len(prices_and_qty_list)):
            subtotal += float(prices_and_qty_list[i][0]) * int(prices_and_qty_list[i][1])
        return round(float(subtotal), 2)

    # This method receives a list of products (price and quantity per product) and calculates total quantity.
    # The list can be created with the method 'add_product_price_and_quantity_to_list()' from ProductPage class
    def calculate_and_return_prod_quantity_in_list(self, prices_and_qty_list):
        qty = 0
        for i in range(len(prices_and_qty_list)):
            qty += int(prices_and_qty_list[i][1])
        return qty

    # The method is useful when working with more than three-digit integer part of a price
    def remove_comma(self, text):
        new_text = ''
        for el in text:
            if el != ",":
                new_text += el
        return new_text

    def get_screen(self, test_description):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        screen_name = f'{now_date}_{test_description}.png'
        self.driver.save_screenshot(
            '.\\screens\\' + screen_name)
