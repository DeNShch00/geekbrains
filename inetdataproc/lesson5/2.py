"""
2) Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД.
 Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import time


def wait_clickable_element_by_class_name(drv, name, timeout_sec=20):
    return WebDriverWait(drv, timeout_sec).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, name))
    )


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
driver.get('https://www.mvideo.ru')

hits_block = None
timeout_sec = 20.0
while timeout_sec > 0:
    products_blocks = driver.find_elements_by_class_name('sel-hits-block')
    if len(products_blocks) < 2:
        time.sleep(0.1)
        timeout_sec -= 0.1
    else:
        hits_block = products_blocks[1]
        break

actions = ActionChains(driver)
actions.move_to_element(hits_block)
actions.perform()

while True:
    try:
        hits_btn_next = wait_clickable_element_by_class_name(hits_block, 'sel-hits-button-next')
        hits_btn_next.click()
        attrs = hits_btn_next.get_attribute('class')
        if 'disabled' in attrs:
            break

    except ElementClickInterceptedException:
        continue
    except TimeoutException:
        break

mongo = MongoClient('localhost', 27017)
db = mongo['mvideo_hits_db']
mvideo_hits_db = db.mvideo_hits

for item in hits_block.find_elements_by_tag_name('li'):
    name = item.find_element_by_class_name('sel-product-tile-title').text
    link = item.find_element_by_class_name('sel-product-tile-title').get_attribute('href')
    price = item.find_element_by_class_name('c-pdp-price__current').text
    # price = int(price.replace(' ', ''))
    # mvideo_hits_db.insert_one({'name': name, 'link': link, 'price': price})
    print({'name': name, 'link': link, 'price': price})

for hit in mvideo_hits_db.find({}):
    print(hit)
