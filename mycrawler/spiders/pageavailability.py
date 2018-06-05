from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mycrawler.items import MycrawlerItem


class PageavailabilitySpider(CrawlSpider):
    handle_httpstatus_list = [400, 403, 404, 500, 502, 503, 504]
    name = 'pageavailability'
    # Replace the value with the real domain.
    allowed_domains = ['example.com']
    # Replace the value with the website URL to crawl from.
    start_urls = ['http://www.example.com/']
    custom_settings = {
        'LOG_FILE': 'logs/pageavailability.log',
        'LOG_LEVEL': 'INFO'
    }

    rules = (
        Rule(
            LinkExtractor(
                allow=('/index/'),
                tags='a',
                attrs='href',
                unique=True
            ),
            callback='parse_item',
            follow=True
        ),
    )

    def parse_item(self, response):
        item = MycrawlerItem()
        item['title'] = response.css('title::text').extract_first()
        item['url'] = response.url
        item['status'] = response.status
        return item
