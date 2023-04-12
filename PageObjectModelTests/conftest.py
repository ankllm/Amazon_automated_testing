from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-US', help="Choose language")
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose language")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()



# d = webdriver.Chrome()
# url = 'https://www.amazon.com/gp/product/B08FCGH2RL/ref=ox_sc_act_image_1?smid=ATVPDKIKX0DER&psc=1'
# d.get(url)
# time.sleep(2)
# el = d.find_element(By.XPATH, '//div[@id="apex_offerDisplay_desktop"]//span[@class="a-price-fraction"]').text
# print(el)