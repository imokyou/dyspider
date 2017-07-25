# -*- coding: utf-8 -*-
import traceback
import scrapy
from dyspider.items import DyspiderItem


class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['http://www.dy2018.com/']

    def parse(self, response):

        vdivs = response.xpath('//div[@class="co_content222"]')
        for index, vdiv in enumerate(vdivs):
            vlist = vdiv.xpath('ul/li')
            for j, snode in enumerate(vlist):
                item = DyspiderItem()

                try:
                    url = snode.xpath('a/@href').extract()[0].encode('utf8')
                    pubdate = snode.xpath('span/font/text()').extract()[0].encode('utf8')

                    item['uid'] = filter(str.isdigit, url)
                    item['name'] = snode.xpath('a/text()').extract()[0].encode('utf8')
                    item['url'] = url
                    item['section'] = index
                    item['category'] = 0
                    item['pubdate'] = '2017-%s' % pubdate

                    yield item
                except:
                    traceback.print_exc()

                
