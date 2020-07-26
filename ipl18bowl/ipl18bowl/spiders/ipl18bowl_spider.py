from scrapy import Spider, Request
from ipl18bowl.items import Ipl18bowlItem


class Ipl18bowlSpider(Spider):
    name = 'ipl18bowl_spider'
    allowed_urls = ['https://www.espncricinfo.com/']
    start_urls = ['https://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=12210;type=tournament']


    def parse(self, response):

        rows = response.xpath('//table[@class="engineTable"]/tbody/tr')

        patterns = ['./td[@class="left"]/a/text()']

        for row in rows:

            for pattern in patterns:
                player = row.xpath(pattern).extract_first()
                if player:
                    break

            if not player:
                continue


            bowl_mat = row.xpath('./td[@class="padAst"]/text()').extract_first()
            bowl_inns = row.xpath('./td[3]//text()').extract_first()
            wkts = row.xpath('./td[7]//text()').extract_first()
            econ = row.xpath('./td[10]//text()').extract_first()
            bowl_sr = row.xpath('./td[11]//text()').extract_first()
            catches = row.xpath('./td[14]//text()').extract_first()


            item = Ipl18bowlItem()
            item['player'] = player
            item['bowl_mat'] = bowl_mat
            item['bowl_inns'] = bowl_inns
            item['wkts'] = wkts
            item['econ'] = econ
            item['bowl_sr'] = bowl_sr
            item['catches'] = catches
            yield item