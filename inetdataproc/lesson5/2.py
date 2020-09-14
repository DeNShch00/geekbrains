"""
2) Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД.
 Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pymongo import MongoClient


# TODO: untested version !!!!


def wait_element_by_class_name(drv, name):
    return WebDriverWait(drv, 20).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, name))
    )


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
url = 'https://www.mvideo.ru'
driver.get(url)

while True:
    try:
        hits_btn = wait_element_by_class_name(driver, 'sel-hits-button-next')
        hits_btn.click()
    except:
        break

mongo = MongoClient('localhost', 27017)
db = mongo['mvideo_hits']
mvideo_hits_db = db.mvideo_hits

for item in driver.find_elements_by_xpath("//div[contains(@class, 'sel-hits-block')]//li"):
    name = item.find_element_by_class_name('sel-product-tile-title').text
    link = url + item.find_element_by_class_name('sel-product-tile-title').get_attribute('href')
    price = item.find_element_by_class_name('c-pdp-price__current').text
    price = int(price.replace(' ', ''))
    mvideo_hits_db.insert_one({'name': name, 'link': link, 'price': price})

for hit in mvideo_hits_db.find({}):
    print(hit)
