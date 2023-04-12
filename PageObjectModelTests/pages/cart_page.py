from pages.locators import *
from selenium.webdriver.common.by import By
from pages.base import Base
from utilities.logger import Logger


class CartPage(Base):

    def click_on_proceed_to_checkout(self):
        self.get_element(*CartLocs.checkout_button).click()
        print('Clicked on checkout button')

    # There's a buybox container on the right of cart page which contains subtotal price
    def return_given_subtotal_in_buybox(self):
        subtotal = self.get_element(*CartLocs.buybox_subtotal).text
        float_subtotal = self.make_price_from_str(subtotal)
        print(f'Subtotal in buybox area is {float_subtotal}')
        return float_subtotal

    # The method receives calculated subtotal price and compares it to the one given in buybox area
    def should_be_correct_subtotal(self, calc_subtotal):
        Logger.add_start_step(method='select_department_and_go_back')
        given_subtotal = self.return_given_subtotal_in_buybox()
        try:
            assert calc_subtotal == given_subtotal
        except AssertionError:
            print(f'\033[31mSubtotal in list: {calc_subtotal} is not equal to subtotal in cart: {given_subtotal}\033[0m')
        print(f'\033[32mSubtotal in list: {calc_subtotal} is equal to subtotal in cart: {given_subtotal}\033[0m')
        Logger.add_end_step(url=self.driver.current_url, method='should_be_correct_subtotal')

    def should_be_products_in_cart(self, prods_list):
        Logger.add_start_step(method='should_be_products_in_cart')
        all_prods_qty_in_list = len(prods_list)
        all_prods_qty_in_cart = len(self.get_elements(*CartLocs.product))
        for i in range(len(prods_list)):
            print(f"\033[36mTrying to find product with price of {prods_list[i][0]} and quantity of {prods_list[i][1]}\033[0m")

            self.is_element_present(By.XPATH, f'//div[@data-price="{prods_list[i][0]}" and @data-quantity="{prods_list[i][1]}"]')

        if all_prods_qty_in_cart != all_prods_qty_in_list:
            print(F'\033[31mThe number of products in list: {all_prods_qty_in_list}; The number of products in cart: {all_prods_qty_in_cart}\033[0m')
        else:
            '\033[32mThe numbers of products in list and in cart coincide\033[0m'
        Logger.add_end_step(url=self.driver.current_url, method='should_be_products_in_cart')

    # There's a buybox container on the right of cart page which contains total quantity of products
    def return_given_items_number_in_buybox(self):
        label = self.get_element(*CartLocs.buybox_label).text
        number = ''
        for i in label:
            if i.isdigit():
                number += i
        print(f'Total number of products in buybox area is  {number}')
        return int(number)

    # The method receives calculated total quantity of products and compares it to the one given in buybox area
    def should_be_correct_items_number_in_buybox_list(self, calc_qty):
        Logger.add_start_step(method='should_be_correct_items_number_in_buybox_list')
        given_items_num = self.return_given_items_number_in_buybox()
        try:
            assert given_items_num == calc_qty
            print(f'\033[32mQuantity in list: {calc_qty} is equal to quantity in cart: {given_items_num}\033[0m')
        except AssertionError:
            print(f'\033[31mQuantity in list: {calc_qty} is not equal to quantity in cart: {given_items_num}\033[0m')
        Logger.add_end_step(url=self.driver.current_url, method='should_be_correct_items_number_in_buybox_list')

    # def return_total_product_quantity_in_cart(self):
    #     qty_elems = self.get_elements(*CartLocs.qty_number_input)
    #     qty_list = self.get_elements_attributes(qty_elems, 'value')
    #     for i in range(len(qty_list)):
    #         qty_list[i] = int(qty_list[i])
    #     return sum(qty_list)

    # def should_be_correct_items_number_in_buybox(self):
    #     given_items_num = self.return_given_items_number_in_buybox()
    #     calc_qty = self.return_total_product_quantity_in_cart()
    #     try:
    #         assert given_items_num == calc_qty
    #         print(f'\033[32m quantity in products container: {calc_qty} is equal to quantity in cart: {given_items_num}\033[0m')
    #     except AssertionError:
    #         print(f'\033[31m quantity in products container: {calc_qty} is not equal to quantity in cart: {given_items_num}\033[0m')
