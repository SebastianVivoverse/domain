import datetime
from segment import Segment
from phenotype import Phenotype
from utils import url_to_id


class Feature:
    def __init__(self,
                 name: str,
                 x: int,
                 y: int,
                 z: int,
                 t: int,
                 user: str,
                 timestamp: datetime.datetime,
                 url: str = None,
                 worm: str = None,
                 worm_image: str = None):

        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.user = user
        self.timestamp = timestamp

        self.url = url
        self.worm = worm
        self.worm_image = worm_image

        self.segmentations: list[Segment] = []
        self.phenotypes: list[Phenotype] = []

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def worm_db_id(self):
        return url_to_id(self.worm)

    @property
    def worm_image_db(self):
        return url_to_id(self.worm_image)

    def to_dict(self):
        return {
            "url": self.url,
            "worm": self.worm,
            "worm_image": self.worm_image,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "t": self.t,
            "user": self.user,
            "timestamp": self.timestamp
        }