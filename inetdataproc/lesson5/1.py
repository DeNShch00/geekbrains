"""
1) Написать программу, которая собирает входящие письма из своего или тестового почтового ящика
 и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
Логин тестового ящика: study.ai_172@mail.ru
Пароль тестового ящика: **********
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pymongo import MongoClient


def wait_element_by_id(drv, id_):
    return WebDriverWait(drv, 20).until(
        expected_conditions.presence_of_element_located((By.ID, id_))
    )


def wait_element_by_class_name(drv, name):
    return WebDriverWait(drv, 20).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, name))
    )


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
driver.get('https://mail.ru/')

login = wait_element_by_id(driver, 'mailbox:login-input')
login.send_keys('study.ai_172')
login.send_keys(Keys.RETURN)

passwd = wait_element_by_id(driver, 'mailbox:password-input')
passwd.send_keys(input('Password: '))
passwd.send_keys(Keys.RETURN)

wait_element_by_class_name(driver, 'js-letter-list-item')
last_letter_id_on_page = last_letter_id_in_box = 0
links_on_letter = set()

while True:
    letters = driver.find_elements_by_class_name('js-letter-list-item')
    if not letters:
        break

    last_letter_id_on_page = letters[-1].get_attribute('data-uidl-id')
    if last_letter_id_on_page == last_letter_id_in_box:
        break
    else:
        last_letter_id_in_box = last_letter_id_on_page

    links_on_letter.update({item.get_attribute('href') for item in letters})

    actions = ActionChains(driver)
    actions.move_to_element(letters[-1])
    actions.perform()

mongo = MongoClient('localhost', 27017)
db = mongo['letters']
letters_db = db.letters

for link in links_on_letter:
    driver.get(link)
    subject = wait_element_by_class_name(driver, 'thread__subject').text
    print(subject)
    date = driver.find_element_by_class_name('letter__date').text
    print(date)
    sender = driver.find_element_by_class_name('letter-contact').get_attribute('title')
    print(sender)
    body = driver.find_element_by_class_name('letter__body').text
    print(body)
    letters_db.insert_one({'subject': subject, 'date': date, 'sender': sender, 'body': body})

for letter in letters_db.find({}):
    print(letter)
