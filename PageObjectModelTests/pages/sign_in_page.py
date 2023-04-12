from pages.locators import SignInLocs
from selenium.webdriver.common.by import By
from pages.base import Base


class SignIn(Base):

    def should_be_signin_form(self):
        print("\033[36mTrying to find sign-in form\033[0m")
        self.is_element_present(*SignInLocs.sign_in_form)

    def should_be_email_or_phone_field(self):
        self.is_element_present(*SignInLocs.email_field)

    def enter_email_or_phone(self, text):
        self.get_element(*SignInLocs.email_field).send_keys(text)

    def click_on_continue_button(self):
        self.get_element(*SignInLocs.continue_button).click()

    # There's an error box above the sign-in form emerging after invalid input.
    # The error message depend on whether the system recognized your input as email or phone number
    def should_be_error_box(self):
        print('\033[36mChecking that the error message box is present\033[0m')
        self.is_element_present(*SignInLocs.sign_in_error_message_box)

    def should_be_correct_inner_error_message_invalid_email_en(self):
        print('\033[36mChecking that the invalid email error message is present\033[0m')
        error_message = self.get_element(*SignInLocs.sign_in_error_message).text
        self.should_be_substring_in_text(SignInLocs.sign_in_error_text_email_en, error_message)

    def should_be_correct_inner_error_message_invalid_email_de(self):
        print('\033[36mChecking that the invalid email error message is present\033[0m')
        error_message = self.get_element(*SignInLocs.sign_in_error_message).text
        self.should_be_substring_in_text(SignInLocs.sign_in_error_text_email_de, error_message)

    def should_be_correct_header_error_message_invalid_phone_en(self):
        print('\033[36mChecking that the invalid phone error message is present\033[0m')
        error_message = self.get_element(*SignInLocs.sign_in_error_message_header).text
        self.should_be_substring_in_text(SignInLocs.sign_in_error_text_header_phone_en, error_message)

    def should_be_correct_header_error_message_invalid_phone_de(self):
        print('\033[36mChecking that the invalid phone error message is present\033[0m')
        error_message = self.get_element(*SignInLocs.sign_in_error_message_header).text
        self.should_be_substring_in_text(SignInLocs.sign_in_error_text_header_phone_de, error_message)

    def should_be_closed_help_expander(self):
        print('\033[36mChecking that the inner contents of help expander are closed \033[0m')
        self.is_element_invisible(*SignInLocs.help_password)
        self.is_element_invisible(*SignInLocs.help_other_issues)

    def expand_help(self):
        self.get_element(*SignInLocs.need_help).click()

    def should_be_expanded_help(self):
        print('\033[36mChecking that the help expander is opened\033[0m')
        self.is_element_visible(*SignInLocs.help_password)
        self.is_element_visible(*SignInLocs.help_other_issues)

    def should_be_create_account_button(self):
        print('\033[36mChecking that the account creation button is present\033[0m')
        self.is_element_present(*SignInLocs.create_account_button)

    def click_on_create_account_button(self):
        self.get_element(*SignInLocs.create_account_button).click()
