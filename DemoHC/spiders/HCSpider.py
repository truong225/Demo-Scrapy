from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from DemoHC.items import DemohcItem


class HCSpider(BaseSpider):
    name = "hc"
    allowed_domains = ["hc.com.vn"]
    start_urls = ["https://hc.com.vn/khuyen-mai/"]

    def parse(self, response):
        khuyenmai = Selector(response).xpath('//li[@class="item"]/div[@class="desc-container"]')

        for sale in khuyenmai:
            item = DemohcItem()
            item['link'] = sale.xpath('h3[@class="saleoff-title"]/a/@href').extract()
            item['title'] = sale.xpath('h3[@class="saleoff-title"]/a/text()').extract()
            item['date'] = sale.xpath('p[@class="saleoff-date"]/text()').extract()



            yield item
