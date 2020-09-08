"""
1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
записывающую собранные вакансии в созданную БД
2) Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введенной суммы.
Поиск по двум полям (мин и макс зарплату)
3) Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта
"""

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup


def num_from_str(s):
    num = [c for c in s if c.isdigit()]
    try:
        return int(''.join(num))
    except ValueError:
        pass

    return None


class MyRequests:
    headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    proxies = {
        'http': 'http://username:password@server:port',
        'https': 'https://username:password@server:port'
    }

    @staticmethod
    def get(url, params):
        return requests.get(url, params=params, headers=MyRequests.headers, proxies=MyRequests.proxies)


class PagedJobSite:
    def __init__(self, url):
        self.url = url

    def _enum_vacancies(self, search_url, req_params):
        while True:
            response = MyRequests.get(search_url, req_params)
            print(f'request: {response.url}\nresponse status: {response.status_code}')
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                vacancy_blocks = self._get_vacancy_blocks(soup)
                for block in vacancy_blocks:
                    yield self._get_vacancy_info(block)

                if self._is_stop_enum_vacancies(soup, vacancy_blocks, req_params):
                    break

                self._next_page(soup, req_params)
            else:
                break

    def _get_vacancy_blocks(self, soup):
        return []

    def _is_stop_enum_vacancies(self, soup, vacancy_blocks, req_params):
        return len(vacancy_blocks) == 0

    def _next_page(self, soup, req_params):
        try:
            req_params['page'] += 1
        except KeyError:
            pass

    def _get_vacancy_info(self, vacancy_block):
        vacancy_id = self._get_vacancy_id(vacancy_block)
        name = self._get_vacancy_name(vacancy_block)
        salary = self._get_vacancy_salary(vacancy_block)
        link = self._get_vacancy_link(vacancy_block)
        return self.url, vacancy_id, name, salary, link

    def _get_vacancy_id(self, vacancy_block):
        return 0

    def _get_vacancy_name(self, vacancy_block):
        return 'unknown'

    def _get_vacancy_salary(self, vacancy_block):
        min_salary = None
        max_salary = None

        return min_salary, max_salary

    def _get_vacancy_link(self, vacancy_block):
        return 'unknown'


class Superjob(PagedJobSite):
    def __init__(self):
        super().__init__('https://www.superjob.ru')

    def get(self, vacancy):
        search_url = self.url + '/vacancy/search/'
        params = {
            'keywords': vacancy,
            'page': 1
        }

        for info in self._enum_vacancies(search_url, params):
            yield info

    def _get_vacancy_blocks(self, soup):
        return soup.find_all('div', {'class': 'f-test-vacancy-item'})

    def _get_vacancy_id(self, vacancy_block):
        for link in vacancy_block.find_all('a'):
            href = link.get('href')
            if href.startswith('/vakansii/'):
                try:
                    return int(href.split('-')[-1].replace('.html', ''))
                except (IndexError, ValueError):
                    print('unknown vacancy_id format: ', href)
                    break

        return 0

    def _get_vacancy_name(self, vacancy_block):
        for link in vacancy_block.find_all('a'):
            if link.get('href').startswith('/vakansii/'):
                return link.getText()

        return 'unknown'

    def _get_vacancy_salary(self, vacancy_block):
        min_salary = None
        max_salary = None
        for salary in vacancy_block.find_all('span', {'class': 'f-test-text-company-item-salary'}):
            text = salary.getText().lower().strip()
            if text and text != 'по договорённости':
                if '—' in text:
                    parts = text.split('—')
                    if len(parts) == 2:
                        min_salary = num_from_str(parts[0].replace(' ', ''))
                        max_salary = num_from_str(parts[1].replace(' ', ''))
                elif 'от ' in text:
                    min_salary = num_from_str(text.replace(' ', ''))
                elif 'до ' in text:
                    max_salary = num_from_str(text.replace(' ', ''))
                elif text[0].isdigit():
                    max_salary = min_salary = num_from_str(text.replace(' ', ''))
                else:
                    print('unknown salary format: ', text)

        return min_salary, max_salary

    def _get_vacancy_link(self, vacancy_block):
        for link in vacancy_block.find_all('a'):
            href = link.get('href')
            if href.startswith('/vakansii/'):
                return self.url + href

        return 'unknown'


class HH(PagedJobSite):
    def __init__(self):
        super().__init__('https://hh.ru')

    def get(self, vacancy):
        search_url = self.url + '/search/vacancy'
        params = {
            'L_is_autosearch': 'false',
            'clusters': 'true',
            'enable_snippets': 'true',
            'search_field': 'name',
            'text': vacancy,
            'page': 0
        }

        for info in self._enum_vacancies(search_url, params):
            yield info

    def _get_vacancy_blocks(self, soup):
        return soup.find_all('div', {'class': 'vacancy-serp-item'})

    def _get_vacancy_id(self, vacancy_block):
        for link in vacancy_block.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'}):
            href = link.get('href')
            try:
                return int(href.split('?')[0].split('/')[-1])
            except (IndexError, ValueError):
                print('unknown vacancy_id format: ', href)
                break

        return 0

    def _get_vacancy_name(self, vacancy_block):
        for link in vacancy_block.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'}):
            return link.getText()

        return 'unknown'

    def _get_vacancy_salary(self, vacancy_block):
        min_salary = None
        max_salary = None
        for salary in vacancy_block.find_all('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}):
            text = salary.getText().lower().strip()
            if text and text != 'по договорённости':
                if '-' in text:
                    parts = text.split('-')
                    if len(parts) == 2:
                        min_salary = num_from_str(parts[0].replace(' ', ''))
                        max_salary = num_from_str(parts[1].replace(' ', ''))
                elif 'от ' in text:
                    min_salary = num_from_str(text.replace(' ', ''))
                elif 'до ' in text:
                    max_salary = num_from_str(text.replace(' ', ''))
                elif text[0].isdigit():
                    max_salary = min_salary = num_from_str(text.replace(' ', ''))
                else:
                    print('unknown salary format: ', text)

        return min_salary, max_salary

    def _get_vacancy_link(self, vacancy_block):
        for link in vacancy_block.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'}):
            return link.get('href')

        return 'unknown'


def json_vacancy_document(site, vacancy_id, name, salary, link):
    doc = {
        'site': site,
        'vacancy_id': vacancy_id,
        'name': name,
        'salary_min': salary[0],
        'salary_max': salary[1],
        'link': link
    }

    return doc


def main():
    mongo = MongoClient('localhost', 27017)
    db = mongo['vacancies']
    vacancies_db = db.vacancies

    while True:
        vacancy = input('Enter vacancy name or "quit" to exit: ')
        if vacancy == 'quit':
            break

        for site, vacancy_id, name, salary, link in Superjob().get(vacancy):
            # Добавляем только новые вакансии с сайта
            if vacancies_db.count_documents({'site': site, 'vacancy_id': vacancy_id}) == 0:
                doc = json_vacancy_document(site, vacancy_id, name, salary, link)
                vacancies_db.insert_one(doc)

        # TODO: Запросы к hh.ru вылетают с ошибкой 404, нужно разобраться почему
        for info in HH().get(vacancy):
            print(info)

    while True:
        salary = input('Enter salary to search vacancy or "quit" to exit: ')
        if salary == 'quit':
            break

        salary = int(salary)
        for vacancy in vacancies_db.find({'$or': [{'salary_min': {"$gt": salary}}, {'salary_max': {'$gt': salary}}]}):
            print(vacancy)


if __name__ == '__main__':
    main()
