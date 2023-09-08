from domain.utils import url_to_id


class Mask:
    def __init__(self,
                 polygon: str,
                 source: str,
                 url: str = None):

        self._polygon = polygon
        self._source = source

        self.url = url

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def polygon(self) -> str:
        return self._polygon

    @property
    def source(self) -> str:
        return self._source

    def to_dict(self):
        return {
            "url": self.url,
            "source": self._source,
            "polygon": self._polygon
        }

    def __repr__(self):
        dictionary = self.to_dict()
        dictionary["class"] = "Mask"
        return f'{dictionary}'


