import datetime
from domain.utils import url_to_id


class Experiment:
    def __init__(self,
                 name: str,
                 chip_capacity: str,
                 chip_material: str,
                 chip_size: str,
                 chip_serial_no: str,
                 acquisition_type: str,
                 scan_date: datetime.datetime,
                 created_on: datetime.datetime,
                 current_round: int,
                 url: str = None,
                 **kwargs):

        self.name = name
        self.chip_capacity = chip_capacity
        self.chip_material = chip_material
        self.chip_size = chip_size
        self.chip_serial_no = chip_serial_no
        self.acquisition_type = acquisition_type
        self.scan_date = scan_date
        self.created_on = created_on
        self.current_round = current_round

        self.url = url

        self.wells = []

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def available_features(self) -> set[str]:

        unique_features = set()
        for well in self.wells:
            for worm in well.worms:
                for worm_image in worm.worm_images:
                    for feature in worm_image.features:
                        unique_features.add(feature.name)

        return unique_features

    def to_dict(self):
        return {
            "url": self.url,
            "name": self.name,
            "chip_capacity": self.chip_capacity,
            "chip_material": self.chip_material,
            "chip_size": self.chip_size,
            "chip_serial_no": self.chip_serial_no,
            "acquisition_type": self.acquisition_type,
            "scan_date": self.scan_date,
            "created_on": str(self.created_on),
            "current_round": self.current_round
        }
