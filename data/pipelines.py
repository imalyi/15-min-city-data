from .validators.POI import POI
from .validators.mevo_stop import Station
from .validators.supermarket import Supermarket
from .validators.stop import Stop
SPIDER_TO_VALIDATOR = {
    'trojmiasto': POI,
    'mevo_stops': Station,
    'supermarkets': Supermarket,
    'stops': Stop,
}


class DataPipeline:
    def process_item(self, item, spider):
        try:
            SPIDER_TO_VALIDATOR.get(spider.name)(**item)
        except ValueError as e:
            print(f"Exception: {e}")
        return item

