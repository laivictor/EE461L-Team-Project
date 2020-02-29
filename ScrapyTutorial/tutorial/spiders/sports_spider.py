import scrapy


class SportsSpider(scrapy.Spider):
    name = "sports"
    start_urls = [
        'https://www.olympic.org/sports'
    ]

    def parse(self, response):
        for sport in response.css('a'):
            yield {
                'href': sport.css('a').get(),
            }
