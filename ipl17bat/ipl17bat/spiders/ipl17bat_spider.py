from scrapy import Spider, Request
from ipl17bat.items import Ipl17batItem


class Ipl17batSpider(Spider):
    name = 'ipl17bat_spider'
    allowed_urls = ['https://www.espncricinfo.com/']
    start_urls = ['https://stats.espncricinfo.com/ci/engine/records/averages/batting.html?id=11701;type=tournament']


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


            bat_mat = row.xpath('./td[@class="padAst"]/text()').extract_first()
            bat_runs = row.xpath('./td[5]//text()').extract_first()
            bat_ave = row.xpath('./td[7]//text()').extract_first()
            bat_sr = row.xpath('./td[9]//text()').extract_first()
            


            item = Ipl17batItem()
            item['player'] = player
            item['bat_mat'] = bat_mat
            item['bat_runs'] = bat_runs
            item['bat_ave'] = bat_ave
            item['bat_sr'] = bat_sr
            yield item