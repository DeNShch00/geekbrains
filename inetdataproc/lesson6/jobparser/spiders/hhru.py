import scrapy
from scrapy.http import HtmlResponse, Request
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?L_save_area=true&clusters=true&enable_snippets=true&text=python&showClusters=true']
    proxy_meta = {"proxy": "https://username:password@server:port"}

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse, meta=self.proxy_meta)

    def parse(self, response: HtmlResponse):
        vacancies = response.css("div.vacancy-serp-item__row_header a.bloko-link::attr(href)").extract()
        for vacancy in vacancies:
            yield response.follow(vacancy, callback=self.vacancy_parse, meta=self.proxy_meta)

        next_page = response.css("a.HH-Pager-Controls-Next::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse, meta=self.proxy_meta)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").extract_first()
        salary = response.xpath("//p[@class='vacancy-salary']//text()").extract()
        yield JobparserItem(name=name, salary=salary)
