from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_departments_list():
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com/')
    WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="nav-hamburger-menu"]'))).click()
    WebDriverWait(driver, 7).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"programs & features")]/preceding::a[@class="hmenu-item hmenu-compressed-btn"]/parent::li'))).click()
    li = []
    i = 1
    elem = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, f'//div[text()="shop by department"]/parent::li/following::a[@class="hmenu-item"][{i}]')))
    while elem != WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//div[text()="programs & features"]/following::a[@class="hmenu-item"][1]'))):
        li.append([elem.text, elem.get_attribute('data-menu-id')])
        i += 1
        elem = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH,
                                   f'//div[text()="shop by department"]/parent::li/following::a[@class="hmenu-item"][{i}]')))
    print(li)

# get_departments_list()

