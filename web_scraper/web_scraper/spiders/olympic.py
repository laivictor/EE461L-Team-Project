

#https://stillmed.olympic.org/media/Images/OlympicOrg/Countries/<LETTER>/<COUNTRY_NAME>/CNO-<ABREV>.jpg

import scrapy 
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


with open('names.json') as f:
	data = json.load(f)

#print(data['country_name'])

class OlympicSpider(CrawlSpider):
	name = 'olympic'
	allowed_domains = ['olympic.org']
	url = 'http://wwww.olympic.org/'
	start_urls = []

	for i in data:
		start_urls.append(url + i['country_name'])

	print(start_urls)
	#start_urls = ['https://stillmed.olympic.org/media/Images/OlympicOrg/Countries']

	rules = (

		    Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),

		    Rule(LinkExtractor(allow=r'/',
		
			),
            callback='parse_item'
            ),
		)


def parse_item(self, response):
        item = {}

        item['img'] = response.xpath('//*[@class = "image alignleft"]//img//src').get()

        print(item['img'])

        return item
