
import scrapy
import json
from typing import Optional


class StopsSpider(scrapy.Spider):
    name = "stops"
    start_urls = \
        ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json']

    def __init__(self, *args, **kwargs):
        super(StopsSpider, self).__init__(*args, **kwargs)
        self.last_update_count = 0

    def parse(self, response):
        data = json.loads(response.text)
        for date, date_data in data.items():
            if 'lastUpdate' in date_data:
                self.last_update_count += 1
                if self.last_update_count == 2:
                    return

            stops = date_data.get("stops")

            if stops:
                for stop in stops:
                    yield {
                        'name': f"{stop.get('stopName', '') or stop.get('stopDesc', '')} {stop.get('stopCode', '')}",
                        'lat': stop.get("stopLat"),
                        'lon': stop.get("stopLon"),
                        'url': "https://ckan.multimediagdansk.pl/"
                    }
