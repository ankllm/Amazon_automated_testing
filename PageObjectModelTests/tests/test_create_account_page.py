from pages.base import Base
from pages.sign_in_page import SignIn
from pages.create_account_page import CreateAccount
import pytest


class TestCreateAccount:

    # @pytest.mark.skip
    def test_should_be_create_account_form(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.should_be_create_account_form()
        sign_in_page.get_screen("create_account_form")

    # @pytest.mark.skip
    def test_should_be_create_business_account_link(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.should_be_create_business_account_link()

    # @pytest.mark.skip
    def test_should_not_create_account_missing_name(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_phone_or_email('+79998889900')
        create_acc_page.enter_password('a_Very_reliable_pa88word')
        create_acc_page.re_enter_password('a_Very_reliable_pa88word')
        create_acc_page.click_on_sign_in_button()
        create_acc_page.should_be_missing_name_error_message()
        create_acc_page.should_be_missing_name_error_style()

    # @pytest.mark.skip
    def test_should_not_create_account_missing_email(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_name('Matriarch Benezia')
        create_acc_page.enter_password('a_Very_reliable_pa88word')
        create_acc_page.re_enter_password('a_Very_reliable_pa88word')
        create_acc_page.click_on_sign_in_button()
        create_acc_page.should_be_missing_email_error_message()
        create_acc_page.should_be_missing_email_error_style()

    # @pytest.mark.skip
    def test_should_not_create_account_missing_password(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_name('Matriarch Benezia')
        create_acc_page.enter_phone_or_email('+79998889900')
        create_acc_page.re_enter_password('a_Very_reliable_pa88word')
        create_acc_page.click_on_sign_in_button()
        create_acc_page.should_be_missing_or_short_password_error_message()
        create_acc_page.should_be_missing_password_error_style()

    # @pytest.mark.skip
    def test_should_not_create_account_missing_password_re_enter(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_name('Matriarch Benezia')
        create_acc_page.enter_phone_or_email('+79998889900')
        create_acc_page.enter_password('a_Very_reliable_pa88word')
        create_acc_page.click_on_sign_in_button()
        create_acc_page.should_be_missing_password_re_enter_error_message()
        create_acc_page.should_be_missing_password_re_enter_error_style()

    # @pytest.mark.skip
    def test_should_not_create_account_invalid_password_re_enter(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_name('Matriarch Benezia')
        create_acc_page.enter_phone_or_email('+79998889900')
        create_acc_page.enter_password('a_Very_reliable_pa88word')
        create_acc_page.re_enter_password('a_very_reliable_pa88word')
        create_acc_page.click_on_sign_in_button()
        create_acc_page.should_be_missing_password_error_style()
        create_acc_page.should_be_invalid_password_re_enter_error_message()
        create_acc_page.should_be_missing_password_re_enter_error_style()

    # @pytest.mark.skip
    def test_should_not_create_account_missing_fields_style(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.click_on_sign_in_button()
        create_acc_page.should_be_missing_name_error_style()
        create_acc_page.should_be_missing_name_error_message()
        create_acc_page.should_be_missing_email_error_style()
        create_acc_page.should_be_missing_email_error_message()
        create_acc_page.should_be_missing_password_error_style()
        create_acc_page.should_be_missing_or_short_password_error_message()
        create_acc_page.should_not_be_error_style_re_enter_password()
        sign_in_page.get_screen("all_fields_missing_errors")

    # @pytest.mark.skip
    def test_should_change_continue_button_style_enter_email(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_phone_or_email('super_cool_cucumber@pochta.ru')
        create_acc_page.unfocus_email_field()
        create_acc_page.should_change_button_style_email()

    # @pytest.mark.skip
    def test_should_change_continue_button_style_enter_phone(self, driver):
        url = 'https://www.amazon.com/'
        base_page = Base(driver, url)
        base_page.open()
        base_page.click_on_sign_in_button()
        sign_in_page = SignIn(driver, driver.current_url)
        sign_in_page.click_on_create_account_button()
        create_acc_page = CreateAccount(driver, driver.current_url)
        create_acc_page.enter_phone_or_email('+79998889900')
        create_acc_page.unfocus_email_field()
        create_acc_page.should_change_button_style_phone()
