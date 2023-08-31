from domain.utils import url_to_id


class BodyMeasurement:
    def __init__(self,
                 length: float,
                 area: float,
                 volume: float = None,
                 url: str = None,
                 mask: str = None,
                 worm: str = None):

        self.length = length
        self.area = area
        self.volume = volume
        self.url = url
        self.mask = mask
        self.worm = worm

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def mask_db_id(self):
        return url_to_id(self.mask)

    @property
    def worm_db_id(self):
        return url_to_id(self.worm)

    def to_dict(self):
        return {
            "url": self.url,
            "length": self.length,
            "area": self.area,
            "volume": self.volume,
            "mask": self.mask,
            "worm": self.worm
        }
