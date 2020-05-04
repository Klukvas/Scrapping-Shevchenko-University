# -*- coding: utf-8 -*-
import scrapy
from abiturientsInfo.items import Abiturient

class AbiturientsSpider(scrapy.Spider):
    name = 'abiturients'
    allowed_domains = ['www.univ.kiev.ua']
    start_urls = ["http://www.univ.kiev.ua/UA/abit/2019/Lists/bachelor"]

    def parse(self, response):
        for num, item in enumerate(response.css('li.b-references__item')):
            link = item.css('a.b-references__link').attrib['href']
            yield response.follow(link, callback=self.specialty)

    def specialty(self, response):
        for num, item in enumerate(response.css('li.b-references__item')):
            link = item.css('a.b-references__link').attrib['href']
            yield response.follow(link, callback=self.get_info)

    def get_info(self, response):

        last_update = response.xpath('/html/body/div[2]/div/div[1]/p/text()'). \
            get().replace('Останнє оновлення: ', '')
        faculty = response.xpath('/html/body/div[2]/div/h3[2]/text()').get()
        specialty = response.xpath('/html/body/div[2]/div/h3[3]/text()').get()
        form = response.xpath('/html/body/div[2]/div/h3[4]/text()').get()
        try:
            license_volume = int(response.xpath('/html/body/div[2]/div/h3[5]/text()').get().split(';')[1])
        except ValueError:
            license_volume = None
        try:
            max_state_order = int(response.xpath('/html/body/div[2]/div/h3[6]/text()').get().split(';')[1])
        except ValueError:
            max_state_order = None
        for item in response.css('tr'):
            abiturItem = Abiturient()
            name = item.xpath('.//td[2]/text()').get()
            try:
                name = name.decode("utf-8")
            except :
                pass
            abiturItem['name'] = name
            abiturItem['mark'] = item.xpath('.//td[3]/text()').get()
            abiturItem['priority'] = item.xpath('.//td[4]/text()').get()
            abiturItem['status'] = item.xpath('.//td[5]/text()').get()
            abiturItem['docs'] = item.xpath('.//td[6]/text()').get()
            abiturItem['faculty'] = faculty
            abiturItem['specialty'] = specialty
            yield abiturItem