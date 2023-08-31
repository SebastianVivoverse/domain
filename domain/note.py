from domain.utils import url_to_id


class Note:
    def __init__(self,
                 text: str,
                 analysis_type: str,
                 user: str,
                 url: str = None,
                 worm_image: str = None):

        self.text = text
        self.analysis_type = analysis_type
        self.user = user

        self.url = url
        self.worm_image = worm_image

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def worm_image_db_id(self):
        return url_to_id(self.worm_image)

    def to_dict(self):
        return {
            "url": self.url,
            "worm_image": self.worm_image,
            "text": self.text,
            "analysis_type": self.analysis_type,
            "user": self.user
        }

    def __repr__(self):
        return f'{self.to_dict()}'
