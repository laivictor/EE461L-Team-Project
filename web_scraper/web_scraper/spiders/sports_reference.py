# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SportsReferenceSpider(CrawlSpider):
    name = 'sports-reference'
    allowed_domains = ['sports-reference.com']
    start_urls = ['http://www.sports-reference.com/olympics/countries']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),

        Rule(LinkExtractor(allow=r'/[A-Z][A-Z][A-Z]',
                        
            ),
            callback='parse_item'
            ),
    )


# run with scrapy crawl --nolog -o - -t json sports-reference 
    def parse_item(self, response):
        item = {}

        item['country'] = response.xpath('//*[@class="float_left margin_right margin_bottom"]//text()').get()
        item['img'] = response.xpath('//p//img//@src').get()
        
        children = []
        for row in response.xpath('//*[@class="sortable  stats_table"]//tbody/tr'):


            children.append({
                'ranker' : row.xpath('td[1]//text()').extract_first(),
                'games' : row.xpath('td[2]//text()').extract_first(),
                'flag_bearer' : row.xpath('td[3]//text()').extract_first(),
                'participants' : row.xpath('td[4]//text()').extract_first(),
                'participants_men' : row.xpath('td[5]//text()').extract_first(),
                'participants_women' : row.xpath('td[6]//text()').extract_first(),
                'sports' : row.xpath('td[7]//text()').extract_first(),
                'Gold' : row.xpath('td[8]//text()').extract_first(),
                'Silver' : row.xpath('td[9]//text()').extract_first(),
                'Bronze' : row.xpath('td[10]//text()').extract_first(),
                'Total' : row.xpath('td[11]//text()').extract_first(),
                'top_medalists' : row.xpath('td[12]//text()').extract_first(),
            })

        item['children'] = children

        return item





