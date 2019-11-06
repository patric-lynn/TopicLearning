import scrapy
import sys
from ..items import WikiscrapyItem

sys.path.append(r'D:\workground\TopicLearning\KTExtraction\ScarpyPackage\wikiscrapy\wikiscrapy')

class WikiCategorySpider(scrapy.Spider):
    name = "wikicat"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Category:Computer_programming"]

    def parse(self, response):
        filename = response.url + '.html'
        with open(filename,'wb')as f:
            f.write(response.body)

        for a in response.xpath('//li'):
            item = WikiscrapyItem.subtitle
            item['subtitle'] = a.xpath('a/text()').extract()
            item['link'] = "https://en.wikipedia.org/" + a.xpath('a/@href').extract()
            yield item