from pages.base import Base
import pytest


class TestHeader:

    # @pytest.mark.skip
    def test_should_be_sign_in_button_in_header(self, driver):
        url = 'https://www.amazon.com/'
        driver.maximize_window()
        base_page = Base(driver, url)
        base_page.open()
        base_page.should_be_sign_in_button_in_header()


class TestMenu:

    # @pytest.mark.skip
    def test_check_department_selection_and_go_back(self, driver):
        url = 'https://www.amazon.com/'
        page = Base(driver, url)
        driver.maximize_window()
        page.open()
        page.open_menu()
        page.see_all_departments()
        page.select_department_and_go_back()
