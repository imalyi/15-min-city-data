import scrapy
import os


class StartURLSFromFile:
    def __init__(self):
        print(os.getcwd())
        with open("start_urls_trojmiasto.txt", "r") as f:
            self.start_urls = f.read().split("\n")


class TrojmiastoSpider(scrapy.Spider):
    name = "trojmiasto"
    start_urls = StartURLSFromFile().start_urls

    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }

    def parse(self, response):
        for poi in response.css("div.basicInfo__item.basicInfo__item--presentationNotPaid"):
            address_info = poi.css("a.objectAddress__link span::text").getall()
            address = {}
            try:
                address["postcode"] = poi.css('.objectAddress__postCode::text').get().strip()
            except AttributeError:
                address["postcode"] = ''
            try:
                address["city"] = poi.css('.objectAddress__city::text').get().strip()
                address["street"] = poi.css('.objectAddress__street::text').get().strip()
            except AttributeError as e:
                address = {}
                self.logger.error(f"Exception: {e}, Address Info: {address_info}, Reason: {str(e)}")

            res = {
                "name": poi.css("h2 a.objectName__link span::text").get(),
                "categories": poi.css("a.objectTags__item::text").getall(),
                "address": address,
                'url': response.url
            }
            yield res
        next_page = response.css('a[title="następna"]::attr("href")').get()

        if next_page:
            yield response.follow(next_page, self.parse)
