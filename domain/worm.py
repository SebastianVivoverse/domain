from domain.utils import url_to_id


class Worm:
    def __init__(self,
                 channel_number: int,
                 well: str = None,
                 url: str = None):

        self.channel_number = channel_number

        self.worm_images = []

        self.url = url
        self.well = well

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def well_db_id(self):
        return url_to_id(self.well)

    def to_dict(self):
        return {
            "url": self.url,
            "well": self.well,
            "channel_number": self.channel_number
        }

    def __repr__(self):
        dictionary = self.to_dict()
        dictionary["worm_images"] = str(self.worm_images)
        return f'{dictionary}'
