# -*- coding: utf-8 -*-
import scrapy

from scrapisos.items import ScrapisosItem

class IdealistaSpider(scrapy.Spider):
    name = 'idealista'
    default_url = 'https://www.idealista.com/'
    allowed_domains = ['www.idealista.com']

    def __init__(self, search='', **kwargs):
        self.start_urls = ['http://www.idealista.com/{}'.format(search)]
        super().__init__(**kwargs)


    def parse(self, response):

        flat_list = response.xpath('//div[@class="item-info-container"]')
        for flat in flat_list:
            title = flat.xpath('./a/text()').extract()

            link = self.default_url + flat.xpath('./a/@href').extract_first()

            price = flat.xpath('./div[@class="row price-row clearfix"]/span[@class="item-price h2-simulated"]/text()') \
                .extract_first(default='0').replace('.', '')

            print("price is {}".format(price))

            rooms_s = flat.xpath("span[@class='item-detail']/small[contains(text(),'hab.')]/../text()").extract_first()
            rooms_i = int(rooms_s) if rooms_s else 0

            m2 = float(flat.xpath('span[@class="item-detail"]/small[starts-with(text(),"m")]/../text()')
                       .extract_first().replace('.', '').strip())

            planta_s = flat.xpath('span[@class="item-detail"]/small[starts-with(text(),"planta")]/../text()').extract_first()
            if planta_s:
                planta_f = float(planta_s[:-2]) # Get rid of the ª
            else:
                planta_f = 0

            ascensor_s = flat.xpath('span[@class="item-detail"]/small[starts-with(text(),"planta")]/text()').extract_first()
            ascensor = 1 if ascensor_s and "con ascensor" in ascensor_s else 0

            flat_item = IdealistaItem(
                title=title,
                link=link,
                price=price,
                rooms=rooms_i,
                m2=m2,
                planta=planta_f,
                ascensor=ascensor,
                comentarios = '{} {}'.format(planta_s, ascensor_s)
            )

            yield flat_item

        next_page = response.xpath('//div[@class="pagination"]//a[@class="icon-arrow-right-after"]/@href') \
            .extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

