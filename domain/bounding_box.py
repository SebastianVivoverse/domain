from domain.utils import url_to_id


class BoundingBox:
    def __init__(self,
                 top_left_x: int,
                 top_left_y: int,
                 bottom_right_x: int,
                 bottom_right_y: int,
                 filepath: str,
                 url: str = None,
                 worm_image: str = None):

        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y
        self.filepath = filepath

        self.url = url
        self.worm_image = worm_image

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def worm_image_db_id(self):
        return url_to_id(self.worm_image)

    @property
    def center(self) -> (int, int):
        center_x = (self.top_left_x + self.bottom_right_x) / 2
        center_y = (self.top_left_y + self.bottom_right_y) / 2
        center = (center_x, center_y)

        return center

    @property
    def top_left_coord(self) -> tuple[int, int]:
        return (self.top_left_x, self.top_left_y)

    @property
    def bottom_right_coord(self) -> tuple[int, int]:
        return (self.bottom_right_x, self.bottom_right_y)

    def to_dict(self):
        return {
            "url": self.url,
            "top_left_x": self.top_left_x,
            "top_left_y": self.top_left_y,
            "bottom_right_x": self.bottom_right_x,
            "bottom_right_y": self.bottom_right_y,
            "filepath": self.filepath,
            "worm_image": self.worm_image
        }

    def __repr__(self):
        dictionary = self.to_dict()
        dictionary["class"] = "BoundingBox"
        return f'{dictionary}'
