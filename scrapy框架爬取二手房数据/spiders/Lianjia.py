import scrapy
from scrapy.http import HtmlResponse
from scrapy import Selector,Request
from Second_house.items import SecondHouseItem

class LianjiaSpider(scrapy.Spider):
    name = 'Lianjia'
    allowed_domains = ['wf.lianjia.com']
    start_urls = ['https://wf.lianjia.com/ershoufang/']

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css('#content > div.leftContent > ul > li')
        for list_item in list_items:
            secondhouse_item = SecondHouseItem()
            secondhouse_item['title'] = list_item.css('div.title a::text').extract_first()
            secondhouse_item['location'] = list_item.css('div.positionInfo a::text').extract_first()
            secondhouse_item['message'] = list_item.css('div.houseInfo::text').extract_first()
            secondhouse_item['total_price'] = list_item.css('div.totalPrice.totalPrice2 span::text').extract_first()
            secondhouse_item['unit_price'] = list_item.css('div.unitPrice span::text').extract_first()
            yield secondhouse_item