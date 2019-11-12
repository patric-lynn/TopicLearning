import scrapy
import sys
from ..items import WikiscrapyItem

sys.path.append(r'D:\workground\TopicLearning\KTExtraction\ScarpyPackage\wikiscrapy\wikiscrapy')

class WikiCategorySpider(scrapy.Spider):
    name = "wikicat"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Category:Computer_programming"]

    def parse(self, response):
        for a in response.xpath('//li'):
            item = WikiscrapyItem()
            item['subtitle'] = a.xpath('a/text()').extract()
            item['link'] = a.xpath('a/@href').extract()
            yield item