import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor is not Vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor Vaccine is Outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor didn`t wear a mask")
        return f"Welcome to {self.name}"
