from domain.utils import url_to_id


class Vertex:
    def __init__(self,
                 x: int,
                 y: int,
                 z: int = None,
                 t: int = None,
                 order: int = None,
                 url: str = None,
                 segment: str = None):

        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.order = order

        self.url = url
        self.segment = segment

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def segment_db_id(self):
        return url_to_id(self.segment)

    def to_dict(self):
        return {
            "url": self.url,
            "segment": self.segment,
            "x": int(self.x),
            "y": int(self.y),
            "z": int(self.z),
            "t": int(self.t),
            "order": self.order
        }

    def __repr__(self):
        dictionary = self.to_dict()
        dictionary["class"] = "Well"
        return f'{dictionary}'
