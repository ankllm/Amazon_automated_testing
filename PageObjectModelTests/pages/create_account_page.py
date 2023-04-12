from pages.locators import CreateAccountLocs
from pages.base import Base


class CreateAccount(Base):

    def should_be_create_account_form(self):
        print('\033[36mTrying to find account creation form\033[0m')
        self.is_element_present(*CreateAccountLocs.create_acc_form)

    def should_be_name_field(self):
        self.is_element_present(*CreateAccountLocs.name_field)

    def should_be_phone_or_email_field(self):
        self.is_element_present(*CreateAccountLocs.phone_or_email_field)

    def should_be_password_field(self):
        self.is_element_present(*CreateAccountLocs.password_field)

    def should_be_password_re_enter_field(self):
        self.is_element_present(*CreateAccountLocs.password_re_enter_field)

    def should_be_continue_button(self):
        self.is_element_present(*CreateAccountLocs.continue_button)

    def should_be_create_business_account_link(self):
        print('\033[36mTrying to find a business acc creation link\033[0m')
        self.is_element_present(*CreateAccountLocs.business_acc_creation_link)

    def enter_name(self, text):
        self.get_element(*CreateAccountLocs.name_field).send_keys(text)
        print(f'Sent {text} into name field')

    def enter_phone_or_email(self, text):
        self.get_element(*CreateAccountLocs.phone_or_email_field).send_keys(text)
        print(f'Sent {text} into email or phone field')

    def enter_password(self, text):
        self.get_element(*CreateAccountLocs.password_field).send_keys(text)
        print(f'Sent {text} into password field')

    def re_enter_password(self, text):
        self.get_element(*CreateAccountLocs.password_re_enter_field).send_keys(text)
        print(f'Sent {text} into password re-enter field')

    def click_on_sign_in_button(self):
        self.get_element(*CreateAccountLocs.continue_button).click()
        print('Clicked on continue button')

    def should_be_missing_name_error_style(self):
        print('\033[36mChecking that the name field is red\033[0m')
        self.is_element_present(*CreateAccountLocs.name_field_error_style)

    def should_be_missing_email_error_style(self):
        print('\033[36mChecking that the email field is red\033[0m')
        self.is_element_present(*CreateAccountLocs.phone_or_email_field_error_style)

    def should_be_missing_password_error_style(self):
        print('\033[36mChecking that the password field is red\033[0m')
        self.is_element_present(*CreateAccountLocs.password_field_error_style)

    def should_be_missing_password_re_enter_error_style(self):
        print('\033[36mChecking that the password re-enter field is red\033[0m')
        self.is_element_present(*CreateAccountLocs.password_re_enter_field_error_style)

    def should_be_missing_name_error_message(self):
        print("\033[36mChecking that there's a missing name error text\033[0m")
        error_message = self.get_element(*CreateAccountLocs.missing_name_error_message).text
        self.should_be_substring_in_text(CreateAccountLocs.missing_name_error_message_text, error_message)

    def should_be_missing_email_error_message(self):
        print("\033[36mChecking that there's a missing email or phone error text\033[0m")
        error_message = self.get_element(*CreateAccountLocs.missing_phone_or_email_error_message).text
        self.should_be_substring_in_text(CreateAccountLocs.missing_phone_or_email_error_message_text, error_message)

    def should_be_missing_or_short_password_error_message(self):
        print("\033[36mChecking that there's a missing or short password error text\033[0m")
        error_message = self.get_element(*CreateAccountLocs.missing_password_error_message).text
        self.should_be_substring_in_text(CreateAccountLocs.missing_or_short_password_error_message_text, error_message)

    def should_be_missing_password_re_enter_error_message(self):
        print("\033[36mChecking that there's a missing or short password re-enter error text\033[0m")
        error_message = self.get_element(*CreateAccountLocs.missing_password_re_enter_error_message).text
        self.should_be_substring_in_text(CreateAccountLocs.missing_password_re_enter_error_message_text, error_message)

    def should_be_invalid_password_re_enter_error_message(self):
        print("\033[36mChecking that there's an invalid password re-enter error text\033[0m")
        error_message = self.get_element(*CreateAccountLocs.invalid_password_re_enter_error_message).text
        self.should_be_substring_in_text(CreateAccountLocs.invalid_password_re_enter_error_message_text, error_message)

    def should_change_button_style_email(self):
        print("\033[36mChecking that the continue button has got 'Verify email' in it\033[0m")
        self.is_element_present(*CreateAccountLocs.continue_button_email_style)

    def should_change_button_style_phone(self):
        print("\033[36mChecking that the continue button has got 'Verify mobile number' in it\033[0m")
        self.is_element_present(*CreateAccountLocs.continue_button_phone_style)

    def should_not_change_button_style_empty_email_or_phone(self):
        print("\033[36mChecking that the continue button has got 'Continue' in it\033[0m")
        self.is_element_present(*CreateAccountLocs.continue_button_empty_phone_or_email_style)

    def unfocus_name_field(self):
        name = self.get_element(*CreateAccountLocs.name_field)
        self.remove_focus(name)

    def unfocus_email_field(self):
        email = self.get_element(*CreateAccountLocs.phone_or_email_field)
        self.remove_focus(email)

    def unfocus_password_field(self):
        password = self.get_element(*CreateAccountLocs.password_field)
        self.remove_focus(password)

    def unfocus_password_re_enter_field(self):
        pass_re_enter = self.get_element(*CreateAccountLocs.password_re_enter_field)
        self.remove_focus(pass_re_enter)

    def should_not_be_error_style_re_enter_password(self):
        print("\033[36mChecking that the password re-enter field isn't red and doesn't have an error message\033[0m")
        self.is_element_not_present(*CreateAccountLocs.password_re_enter_field_error_style)
        self.is_element_invisible(*CreateAccountLocs.invalid_password_re_enter_error_message)
