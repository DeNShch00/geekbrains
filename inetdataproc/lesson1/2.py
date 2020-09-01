"""
2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
 Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

 В качестве открытого API выбран API Геокодера Яндекс Карт.
 https://tech.yandex.ru/maps/geocoder/doc/desc/concepts/about-docpage/
 Этот API позволяет определять координаты объекта по его адресу, или адрес объекта по его координатам.
 Example:
    Чтобы определить координаты здания по адресу "ул. Тверская, дом 7" (здание Центрального Телеграфа в Москве),
    можно выполнить следующий запрос:
        https://geocode-maps.yandex.ru/1.x/?apikey=ваш API-ключ&geocode=Москва,+Тверская+улица,+дом+7
    В ответе геокодера будут географические координаты этого здания, а также дополнительная информация
     о найденном объекте (см. страницу Ответ геокодера).
    При обратном геокодировании в запросе указываются координаты искомого объекта:
        https://geocode-maps.yandex.ru/1.x/?apikey=ваш API-ключ&geocode=37.597576,55.771899
"""

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.135 Safari/537.36'}

proxies = {
 'http': 'http://username:password@server:port',
 'https': 'https://username:password@server:port'
}

url = f'https://geocode-maps.yandex.ru/1.x/'

basic_params = {
    'apikey': 'c47ff388-df6f-4a2c-8a33-cc51bf50e750',
    'sco': 'longlat',
    'format': 'json',
    'results': 5,
    'lang': 'ru_RU'
}

while True:
    coordinates = input('Enter coordinates <longitude, latitude> "quit" to exit: ')
    if coordinates == 'quit':
        break

    params = basic_params.copy()
    params['geocode'] = coordinates

    response = requests.get(url, headers=headers, params=params, proxies=proxies)
    print(f'request: {response.url}\nresponse status: {response.status_code}')
    if response.ok:
        name = 'Map info ' + coordinates.replace(',', '_').replace('.', '_')
        with open(f'{name}.json', 'w', encoding='utf-8') as file:
            file.write(response.content.decode('utf-8'))
