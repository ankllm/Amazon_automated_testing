from pages.locators import ShoppingPageFilterLocs
from pages.shopping_page import ShoppingPage
import pytest


class TestShoppingPageFilters:

    # @pytest.mark.skip
    def test_check_brand_filters(self, driver):
        url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011&ref=nav_em__nav_desktop_sa_intl_monitors_0_2_6_8'
        page = ShoppingPage(driver, url)
        page.open()
        page.check_brand_filter()

    # @pytest.mark.skip
    def test_check_price_filter_25_50(self, driver):
        url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225006011&rh=n%3A%2116225006011%2Cn%3A11060451&ref=nav_em__nav_desktop_sa_intl_skin_care_0_2_11_3'
        page = ShoppingPage(driver, url)
        page.open()
        page.select_price_filter(*ShoppingPageFilterLocs.price_filter_25_50)
        page.should_be_correct_prices_on_shopping_page(25, 49.99)
