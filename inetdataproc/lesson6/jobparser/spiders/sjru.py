import scrapy
from scrapy.http import HtmlResponse, Request
from jobparser.items import JobparserItem


class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4']
    proxy_meta = {"proxy": "https://username:password@server:port"}

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse, meta=self.proxy_meta)

    def parse(self, response: HtmlResponse):
        vacancies = response.css("div.f-test-vacancy-item a::attr(href)").extract()
        for vacancy in vacancies:
            if vacancy.startswith('/vakansii/'):
                yield response.follow('https://www.superjob.ru' + vacancy, callback=self.vacancy_parse, meta=self.proxy_meta)

        next_page = response.css("a.f-test-button-dalshe::attr(href)").extract_first()
        if next_page:
            yield response.follow('https://www.superjob.ru' + next_page, callback=self.parse, meta=self.proxy_meta)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").extract_first()
        salary = response.xpath("//span[contains(@class, '_1OuF_ ZON4b')]//text()").extract()
        yield JobparserItem(name=name, salary=salary)
