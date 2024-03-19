import scrapy
import json


class MevoSpider(scrapy.Spider):
    name = "mevo_stops"
    start_urls = [
        'https://gbfs.urbansharing.com/rowermevo.pl/station_information.json'
    ]

    def parse(self, response):
        data = json.loads(response.body)
        for station in data['data']['stations']:
            yield {
                'lat': station.get('lat'),
                'lon': station.get('lon'),
                'categories': ['MEVO', 'Bike stop']
            }
