import datetime
from domain.utils import url_to_id


class Phenotype:
    def __init__(self,
                 name: str,
                 score: str,
                 user: str,
                 timestamp: datetime.datetime,
                 url: str = None,
                 feature: str = None):

        self.name = name
        self.score = score
        self.user = user
        self.timestamp = timestamp

        self.url = url
        self.feature = feature

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def feature_db_id(self):
        return url_to_id(self.feature)

    def to_dict(self):
        return {
            "url": self.url,
            "feature": self.feature,
            "name": self.name,
            "score": self.score,
            "user": self.user,
            "timestamp": str(self.timestamp)
        }

    def __repr__(self):
        return f'{self.to_dict()}'
