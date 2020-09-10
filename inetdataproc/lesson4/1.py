"""
Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex-новости.
Для парсинга использовать XPath. Структура данных должна содержать:
название источника;
наименование новости;
ссылку на новость;
дата публикации.
"""


import requests
from lxml import html
from abc import ABC, abstractmethod
import datetime
from pprint import pprint


class MyRequests:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    proxies = {
        'http': 'http://username:password@server:port',
        'https': 'https://username:password@server:port'
    }

    @staticmethod
    def get(url, params):
        return requests.get(url, params=params, headers=MyRequests.headers, proxies=MyRequests.proxies)


class NewsSite(ABC):
    def __init__(self, url):
        self.url = url

    def get_news(self):
        return self._get_news(self.url, dict())

    def _get_news(self, news_url, req_params):
        response = MyRequests.get(news_url, req_params)
        print(f'request: {response.url}\nresponse status: {response.status_code}')
        if response.ok:
            return self._parse_news(response.text)

    @abstractmethod
    def _parse_news(self, html_doc):
        pass


class MailRuNews(NewsSite):
    def __init__(self):
        super().__init__('https://news.mail.ru/')

    def _parse_news(self, html_doc):
        news = []
        dom = html.fromstring(html_doc)
        for item in dom.xpath("//div[contains(@class, 'newsitem ')]"):
            name = item.xpath(".//span[contains(@class, 'newsitem__title-inner')]/text()")[0]
            link = item.xpath(".//a[contains(@class, 'newsitem__title')]/@href")[0]
            params = item.xpath(".//div[@class='newsitem__params']")[0]
            date = params.xpath(".//span[1]/@datetime")[0]
            date = date.replace('T', ' ')
            date = ''.join(date.rsplit(':', 1))
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S%z')
            source = params.xpath(".//span[2]/text()")[0]
            news.append({'name': name, 'link': link, 'date': date, 'source': source})

        return news


class LentaNews(NewsSite):
    def __init__(self):
        super().__init__('https://lenta.ru/')

    def _parse_news(self, html_doc):
        news = []
        dom = html.fromstring(html_doc)
        for item in dom.xpath("//div[contains(@class, 'item news')]"):
            name = item.xpath(".//a/span/text()")[0]
            link = item.xpath(".//a/@href")[0]
            if link.startswith('/'):
                link = self.url + link

            time = item.xpath(".//span[@class='time']/text()")[0]
            hours, minutes = time.split(':')
            time = datetime.time(int(hours), int(minutes))

            date = item.xpath(".//span[contains(@class, 'item__date')]/text()")[0]
            if date == 'Сегодня':
                date = datetime.date.today()
                date = datetime.datetime.combine(date, time)
            else:
                # TODO: add parse other dates
                date = 'unknown'

            news.append({'name': name, 'link': link, 'date': date, 'source': 'unknown'})

        return news


class YandexNews(NewsSite):
    def __init__(self):
        super().__init__('https://yandex.ru/news/')

    def _parse_news(self, html_doc):
        news = []
        # TODO: add parse here

        return news


def main():
    pprint(MailRuNews().get_news())
    pprint(LentaNews().get_news())
    pprint(YandexNews().get_news())


if __name__ == '__main__':
    main()
