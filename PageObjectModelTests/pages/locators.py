from selenium.webdriver.common.by import By


departments_dict_en = {'Electronics': 5, 'Computers': 6, 'Smart Home': 7, 'Arts & Crafts': 8, 'Automotive': 9, 'Baby': 10,
                        'Beauty and personal care': 11, "Women's Fashion": 12, "Men's Fashion": 13, "Girls' Fashion": 14,
                        "Boys' Fashion": 15, 'Health and Household': 16, 'Home and Kitchen': 17, 'Industrial and Scientific': 18,
                        'Luggage': 19, 'Movies & Television': 20, 'Pet supplies': 21, 'Software': 22, 'Sports and Outdoors': 23,
                        'Tools & Home Improvement': 24, 'Toys and Games': 25, 'Video Games': 26}

departments_list_en = [['Electronics', '5'], ['Computers', '6'], ['Smart Home', '7'], ['Arts & Crafts', '8'],
                       ['Automotive', '9'], ['Baby', '10'], ['Beauty and personal care', '11'], ["Women's Fashion", '12'],
                       ["Men's Fashion", '13'], ["Girls' Fashion", '14'], ["Boys' Fashion", '15'],
                       ['Health and Household', '16'], ['Home and Kitchen', '17'], ['Industrial and Scientific', '18'],
                       ['Luggage', '19'], ['Movies & Television', '20'], ['Pet supplies', '21'], ['Software', '22'],
                       ['Sports and Outdoors', '23'], ['Tools & Home Improvement', '24'], ['Toys and Games', '25'],
                       ['Video Games', '26']]

departments_numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
departments_numbers_for_random_choice_tests = [5, 6]


class HeaderLocs:

    sign_in = (By.XPATH, '//a[@id ="nav-link-accountList"]')
    sign_in_inner_button = (By.XPATH, '//a[@data-nav-ref="nav_signin"]')
    cart = (By.XPATH, '//a[@id="nav-cart"]')
    cart_products_number = (By.XPATH, '//span[@id="nav-cart-count"]')


class SignInLocs:

    sign_in_form = (By.XPATH, '//form[@name="signIn"]')

    email_field = (By.XPATH, '//input[@type="email"]')
    continue_button = (By.XPATH, '//input[@id="continue"]')
    password_field = (By.XPATH, '//input[@type="password"]')
    sign_in_button = (By.XPATH, '//input[@id="signInSubmit"]')

    sign_in_error_message_header = (By.XPATH, '//h4[@class="a-alert-heading"]')
    sign_in_error_message_box = (By.XPATH, '//div[@id="auth-error-message-box"]')
    sign_in_error_message = (By.XPATH, '//div[@id="auth-error-message-box"]//span')

    sign_in_error_text_email_en = 'We cannot find an account with that email address'
    sign_in_error_text_email_de = 'Es konnte kein Konto mit dieser E-Mail-Adresse gefunden werden.'

    sign_in_error_text_header_phone_en = 'Incorrect phone number'
    sign_in_error_text_header_phone_de = 'Falsche Telefonnummer'



    # sign_in_error_message_text_en = (By.XPATH, '')
    # sign_in_error_message_text_de = (By.XPATH, '')

    create_account_button = (By.XPATH, '//a[@id="createAccountSubmit"]')

    need_help = (By.XPATH, '//span[contains(text(), "Need help?")]')
    need_help_expander = (By.XPATH, '//span[contains(text(), "Need help?")]/parent::a')
    help_password = (By.XPATH, '//a[contains(text()," Forgot your password?")]')
    help_other_issues = (By.XPATH, '//a[contains(text(),"Other issues with Sign-In")]')


class CreateAccountLocs:

    create_acc_form = (By.XPATH, '//form[@id="ap_register_form"]')
    name_field = (By.XPATH, '//input[@name="customerName"]')
    phone_or_email_field = (By.XPATH, '//input[@name="email"]')
    password_field = (By.XPATH, '//input[@name="password"]')
    password_re_enter_field = (By.XPATH, '//input[@name="passwordCheck"]')
    continue_button = (By.XPATH, '//input[@id="continue"]')
    continue_button_empty_phone_or_email_style = (By.XPATH, '//span[@class="default-text" and text()="Continue"]')
    continue_button_phone_style = (By.XPATH, '//span[@class="phone-text" and text()="Verify mobile number"]')
    continue_button_email_style = (By.XPATH, '//span[@class="email-text" and text()="Verify email"]')
    business_acc_creation_link = (By.XPATH, '//a[@id="ab-registration-link"]')

    name_field_error_style = (By.XPATH, '//input[@name="customerName" and contains(@class, "error")]')
    missing_name_error_message = (By.XPATH, '//div[@id="auth-customerName-missing-alert"]')
    missing_name_error_message_text = 'Enter your name'

    phone_or_email_field_error_style = (By.XPATH, '//input[@name="email" and contains(@class, "error")]')
    missing_phone_or_email_error_message = (By.XPATH, '//div[@id="auth-email-missing-alert"]')
    missing_phone_or_email_error_message_text = 'Enter your email or mobile phone number'

    password_field_error_style = (By.XPATH, '//input[@name="password" and contains(@class, "error")]')
    missing_password_error_message = (By.XPATH, '//div[@id="auth-password-missing-alert"]')
    missing_or_short_password_error_message_text = 'Minimum 6 characters required'

    password_re_enter_field_error_style = (By.XPATH, '//input[@name="passwordCheck" and contains(@class, "error")]')
    missing_password_re_enter_error_message = (By.XPATH, '//div[@id="auth-passwordCheck-missing-alert"]')
    missing_password_re_enter_error_message_text = 'Type your password again'
    invalid_password_re_enter_error_message = (By.XPATH, '//div[@id="auth-password-mismatch-alert"]')
    invalid_password_re_enter_error_message_text = 'Passwords must match'


class MenuLocs:

    menu_button = (By.XPATH, '//a[@id="nav-hamburger-menu"]')
    menu = (By.XPATH, '//ul[@data-menu-id="1"]')
    close_menu = (By.XPATH, '//div[contains(@class, "hmenu-close-icon")]')
    see_all_departments = (By.XPATH, '//div[contains(text(),"programs & features")]/preceding::a[@class="hmenu-item hmenu-compressed-btn"]/parent::li')

    #subdepartment = (By.XPATH, '//*[@data-menu-id="11"]//a[@class="hmenu-item"]')

    #back_to_menu_from_department = (By.XPATH, f'//a[@data-ref-tag ="nav_em_1_{departments_dict_en[department_name]}_BT_0_main_menu"]')


class ShoppingPageFilterLocs:

    brand_old = (By.XPATH, '//li[contains(@id, "p_89/")]//a')
    brand_new = (By.XPATH, '//span[text()="Brand"]/parent::div/following-sibling::ul/descendant::li//a')

    subdepartment = (By.XPATH, '//span[contains(@class, "refinements-indent")]')

    price_filter_under_25 = (By.XPATH, '//span[text()="Under $25"]')
    price_filter_25_50 = (By.XPATH, '//span[text()="$25 to $50"]')
    price_filter_50_100 = (By.XPATH, '//span[text()="$50 to $100"]')
    price_filter_100_200 = (By.XPATH, '//span[text()="$100 to $200"]')
    price_filter_200_and_above = (By.XPATH, '//span[text()="$200 & Above"]')

    price_filter_range_min = (By.XPATH, '//input[@id="low-price"]')
    price_filter_range_max = (By.XPATH, '//input[@id="high-price"]')
    price_filter_range_go = (By.XPATH, '//span[contains(@class, "a-button-base")]')


class ShoppingPageProductsLocs:

    products_container = (By.XPATH, '//div[contains(@class, "s-main-slot")]')
    available_product = (By.XPATH, '//span[contains(text(), "Ships to")]/ancestor::div[@data-component-type="s-search-result"]')
    available_prod_image = (By.XPATH, '//span[contains(text(), "Ships to")]/ancestor::div[@data-component-type="s-search-result"]//div[contains(@class,"product-image")]')
    product_title = (By.XPATH, '//span[contains(text(), "Ships to")]/ancestor::div[@data-component-type="s-search-result"]//h2')
    price_symbol = (By.XPATH, '//span[@class="a-price-symbol"]')
    price_whole = (By.XPATH, '//span[@class="a-price-whole"]')
    price_fraction = (By.XPATH, '//span[@class="a-price-fraction"]')


class ProductPageLocs:

    product_price_whole_box = (By.XPATH, '//div[@id="apex_offerDisplay_desktop"]//span[@class="a-price-whole"]')
    product_price_fraction_box = (By.XPATH, '//div[@id="apex_offerDisplay_desktop"]//span[@class="a-price-fraction"]')
    prod_title = (By.XPATH, '//span[@id="productTitle"]')
    product_brand = (By.XPATH, '//tr[contains(@class, "po-brand")]/td[2]/span]')

    add_to_cart_button = (By.XPATH, '//input[@id="add-to-cart-button"]')
    buy_now_button = (By.XPATH, '//input[@id="buy-now-button"]')

    quantity_select = (By.XPATH, '//div[@class="a-column a-span12 a-text-left"]/span')
    quantity_option = (By.XPATH, '//select[@name="quantity"]/option')

    department = (By.XPATH, '//a[contains(@href, "/b/ref")])')
    subdepartment = (By.XPATH, '//a[contains(@href, "/s/ref"]')
    # warranty_pane = (By.XPATH, '')
    warranty_pane = (By.XPATH, '//div[@id="attach-warranty-display"]')
    warranty_pane_refuse_button = (By.XPATH, '//input[@aria-labelledby="attachSiNoCoverage-announce"]')
    warranty_pane_close = (By.XPATH, '//a[@id="attach-close_sideSheet-link"]')
    warranty_pane_cart_button = (By.XPATH, '//input[@aria-labelledby="attach-sidesheet-view-cart-button-announce"]')
    warranty_pane_checkout_button = (By.XPATH, '//input[@aria-labelledby="attach-sidesheet-checkout-button-announce"]')


class AddedToCartLocs:

    added_to_cart_msg = (By.XPATH, '//span[contains(text(), "Added to Cart")]')

    price_symbol = (By.XPATH, '//*[contains(@class,"subtotal")]//*[@class="a-price-symbol"]')
    price_whole = (By.XPATH, '//*[contains(@class,"subtotal")]//*[@class="a-price-whole"]')
    price_fraction = (By.XPATH, '//*[contains(@class,"subtotal")]//*[@class="a-price-fraction"]')

    checkout_button = (By.XPATH, '//input[@name="proceedToRetailCheckout"]')
    checkout_button_label = (By.XPATH, '//div[@data-feature-id="proceed-to-checkout-label"]')
    go_to_cart_button = (By.XPATH, '//a[@data-csa-c-content-id="sw-gtc_CONTENT"]')
    sign_in_message = (By.XPATH, '//div[@id="sw-atc-buy-box-sign-in-message"]')
    sign_in_link = (By.XPATH, '//div[@id="sw-atc-buy-box-sign-in-message"]//a')


class CartLocs:

    products_container = (By.XPATH, '//div[@data-name="Active Items"]')

    product = (By.XPATH, '//div[@data-name="Active Items"]/div[@data-asin]')
    product_price = (By.XPATH, '//span[contains(@class, "sc-product-price")]')
    product_title = (By.XPATH,
                     '//div[@data-name="Active Items"]//span[@class="a-truncate sc-grid-item-product-title a-size-base-plus"]//span[@class="a-truncate-full a-offscreen"]')

    quantity_select = (By.XPATH, '//select[@name="quantity"]')
    quantity_option = (By.XPATH, '//select[@name="quantity"]/option')
    # quantity_selected_option = (By.XPATH, '//li[@aria-checked="true"]')
    qty_number_select = (By.XPATH, '//span[@class="a-dropdown-prompt"]')
    qty_number_input = (By.XPATH, '//input[@name="quantityBox"]')

    buybox_label = (By.XPATH, '//span[@id="sc-subtotal-label-buybox"]')
    buybox_subtotal = (By.XPATH, '//span[@id="sc-subtotal-amount-buybox"]/span')
    products_container_label = (By.XPATH, '//span[contains( @ id, "label-activecart")]')
    products_container_subtotal = (By.XPATH, '//span[contains(@id, "activecart")]/span')
    checkout_button = (By.XPATH, '//input[@name="proceedToRetailCheckout"]')


# class DepartmentsLocators:
#     monitors = (By.XPATH, '//a[text()="Monitors"]')
#     skin_care = (By.XPATH, '//a[text()="Skin Care"]')
