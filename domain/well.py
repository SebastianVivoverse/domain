from domain.worm import Worm
from domain.utils import url_to_id

class Well:
    def __init__(self,
                 row: int,
                 column: str,
                 animal_strain: str,
                 animal_age: str,
                 drug_name: str,
                 drug_concentration: str,
                 solvent_name: str,
                 solvent_concentration: str,
                 experiment: str = None,
                 url: str = None):

        self.row = row
        self.column = column
        self.animal_strain = animal_strain
        self.animal_age = animal_age
        self.drug_name = drug_name
        self.drug_concentration = drug_concentration
        self.solvent_name = solvent_name
        self.solvent_concentration = solvent_concentration

        self.url = url
        self.experiment = experiment

        self.worms: list[Worm] = []

    @property
    def db_id(self):
        return url_to_id(self.url)

    @property
    def experiment_db_id(self):
        return url_to_id(self.experiment)

    def to_dict(self):
        return {
            "url": self.url,
            "experiment": self.experiment,
            "row": self.row,
            "column": self.column,
            "animal_strain": self.animal_strain,
            "animal_age": self.animal_age,
            "drug_name": self.drug_name,
            "drug_concentration": self.drug_concentration,
            "solvent_name": self.solvent_name,
            "solvent_concentration": self.solvent_concentration
        }

    def __repr__(self):
        dictionary = self.to_dict()
        dictionary["worms"] = str(self.worms)
        return f'{dictionary}'
