import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroymerlinparser.items import LeroymerlinparserItem
from pprint import pprint

class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}&suggest=true']
        super().__init__()

    def parse(self, response: HtmlResponse):
        for link in response.xpath("//a[@slot='name']"):
            yield response.follow(link, callback=self.product_parse)

        for link in response.xpath("//a[contains(@class, 'next-paginator-button')]"):
            yield response.follow(link, callback=self.parse)
            break

    def product_parse(self, response: HtmlResponse):
        # name = response.xpath("//h1/text()").extract_first()
        # price = response.xpath("//span[@slot='price']/text()").extract_first()
        # photos = response.xpath("//img[@alt='product image']/@src").extract()
        # props_names = response.xpath("//div[@class='def-list__group']//dt/text()").extract()
        # props_values = response.xpath("//div[@class='def-list__group']//dd/text()").extract()
        # pprint((response.url, name, str(price), photos, props_names, props_values))

        loader = ItemLoader(item=LeroymerlinparserItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('photos', "//img[@alt='product image']/@src")
        loader.add_xpath('props_names', "//div[@class='def-list__group']//dt/text()")
        loader.add_xpath('props_values', "//div[@class='def-list__group']//dd/text()")
        yield loader.load_item()
