import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
            "https://www.lagou.com"
            ]

    def parse(self, response):
        for sel in response.xpath('//p'):
            item = DmozItem()
            item['link'] = sel.xpath('text()').extract()
            item['title'] = sel.xpath('//span/text()').extract()

            yield item

