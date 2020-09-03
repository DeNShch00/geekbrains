"""
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы)
 с сайтов Superjob и HH.
 Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
 Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (отдельно минимальную и максимальную).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия.
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
Структура должна быть одинаковая для вакансий с обоих сайтов.
Общий результат можно вывести с помощью dataFrame через pandas.
"""

# https://krasnogorsk.hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&search_field=name&text=%D1%81%D0%B0%D0%BD%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA&page=38

import requests


url_hh = 'https://krasnogorsk.hh.ru/search/vacancy'
params_hh = {
    'L_is_autosearch': 'false',
    'clusters': 'true',
    'enable_snippets': 'true',
    'search_field': 'name',
    'text': None
}

headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                        ' (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

while True:
    vacancy = input('Enter vacancy name or "quit" to exit: ')
    if vacancy == 'quit':
        break

    params_hh['text'] = vacancy
    u2 = 'https://krasnogorsk.hh.ru/search/vacancy?L_save_area=true&clusters=true&enable_snippets=true&search_field=name&text=%D1%83%D1%87%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&showClusters=true'
    # response = requests.get(url_hh, headers=headers, params=params_hh)
    u2 = 'https://krasnogorsk.hh.ru/employer/1006181'
    response = requests.get(u2, headers=headers)
    print(f'request: {response.url}\nresponse status: {response.status_code}')
    print(response.status_code)





# from bs4 import BeautifulSoup as bs
# import requests
# from pprint import pprint
#
#
# main_link = 'https://www.kinopoisk.ru'
# headers = {'User_Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
#                          '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
#
# response = requests.get(main_link + '/popular/films/?quick_filters=serials&tab=all',headers=headers)
# soup = bs(response.text,'html.parser')
#
# # serials_block = soup.find('div',{'class':'selection-list'})
# # serials_list = serials_block.findChildren(recursive=False)
# serials_list = soup.find_all('div',{'class':'desktop-rating-selection-film-item'})
#
# serials = []
# for serial in serials_list:
#     serial_data={}
#     serial_link = main_link + serial.find('a', class_='selection-film-item-meta__link').get('href')
#     serial_name = serial.find('p').getText()
#     serial_genre = serial.find('span',
#                                class_='selection-film-item-meta__meta-additional-item').find_next_sibling().getText()
#     try:
#         serial_rating = serial.find('span',class_='rating__value').getText()
#     except:
#         serial_rating = 0
#
#     serial_data['name'] = serial_name
#     serial_data['link'] = serial_link
#     serial_data['genre'] = serial_genre
#     serial_data['rating'] = serial_rating
#
#     serials.append(serial_data)
#
# pprint(serials)