from pages.base import Base
from pages.sign_in_page import SignIn
import pytest


class TestSignIn:

    # @pytest.mark.skip
    def test_should_be_closed_need_help_expander(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.should_be_closed_help_expander()

    # @pytest.mark.skip
    def test_should_open_need_help_expander(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.expand_help()
        sign_in_page.should_be_expanded_help()

    # @pytest.mark.skip
    def test_should_be_create_account_button(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.should_be_create_account_button()

    # @pytest.mark.skip
    @pytest.mark.eng
    def test_should_be_error_message_invalid_email_en(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.enter_email_or_phone('b@4')
        sign_in_page.click_on_continue_button()
        sign_in_page.should_be_error_box()
        sign_in_page.should_be_correct_inner_error_message_invalid_email_en()
        sign_in_page.get_screen("invalid_email_err_msg_en")

    @pytest.mark.de
    # @pytest.mark.skip
    def test_should_be_error_message_invalid_email_de(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.enter_email_or_phone('b@4')
        sign_in_page.click_on_continue_button()
        sign_in_page.should_be_error_box()
        sign_in_page.should_be_correct_inner_error_message_invalid_email_de()
        sign_in_page.get_screen("invalid_email_err_msg_de")


    @pytest.mark.eng
    def test_should_be_correct_header_error_message_invalid_phone_en(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.enter_email_or_phone('5634')
        sign_in_page.click_on_continue_button()
        sign_in_page.should_be_error_box()
        sign_in_page.should_be_correct_header_error_message_invalid_phone_en()
        sign_in_page.get_screen("invalid_phone_err_msg_en")

    @pytest.mark.de
    # @pytest.mark.skip
    def test_should_be_correct_header_error_message_invalid_phone_de(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.enter_email_or_phone('5634')
        sign_in_page.click_on_continue_button()
        sign_in_page.should_be_error_box()
        sign_in_page.should_be_correct_header_error_message_invalid_phone_de()
        sign_in_page.get_screen("invalid_phone_err_msg_de")

