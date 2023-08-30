from domain.feature import Feature
from domain.note import Note
from domain.bounding_box import BoundingBox
from domain.utils import url_to_id


class WormImage:
    def __init__(self,
                 source: str,
                 illumination: str,
                 objective: str,
                 time_lapse: str,
                 filepath: str,
                 worm: str = None,
                 url: str = None):

        self.source = source
        self.illumination = illumination
        self.objective = objective
        self.time_lapse = time_lapse
        self.filepath = filepath

        self.url = url
        self.worm = worm

        self.features: list[Feature] = []
        self.notes: list[Note] = []
        self.bounding_boxes: list[BoundingBox] = []

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def well_db_id(self):
        return url_to_id(self.worm)

    def to_dict(self):
        return {
            "url": self.url,
            "worm": self.worm,
            "source": self.source,
            "illumination": self.illumination,
            "objective": self.objective,
            "time_lapse": self.time_lapse,
            "filepath": self.filepath
        }
