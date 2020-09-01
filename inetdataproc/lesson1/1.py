"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
 сохранить JSON-вывод в файле *.json.
"""

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.135 Safari/537.36'}

proxies = {
 'http': 'http://username:password@server:port',
 'https': 'https://username:password@server:port'
}

while True:
    user_name = input('Enter GitHub user name or "quit" to exit: ')
    if user_name == 'quit':
        break

    url = f'https://api.github.com/users/{user_name}/repos'
    response = requests.get(url, headers=headers, proxies=proxies)
    print(f'request: {response.url}\nresponse status: {response.status_code}')
    if response.ok:
        j_data = response.json()
        if isinstance(j_data, list):
            print('repos count: ', len(j_data))
            for num, repo in enumerate(j_data):
                print(f'{num}\t{repo["full_name"]}\t{repo["description"]}')

        with open(f'{user_name}.json', 'w', encoding='utf-8') as file:
            file.write(response.content.decode('utf-8'))
