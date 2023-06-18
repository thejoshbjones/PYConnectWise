from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
class LevelOne(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelTwo(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelThree(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelFour(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelFive(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelSix(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'

class TaxCodeXRefModel(ConnectWiseModel):
    id: int | None
    description: str | None
    default_flag: bool | None
    level_one: LevelOne | None
    level_two: LevelTwo | None
    level_three: LevelThree | None
    level_four: LevelFour | None
    level_five: LevelFive | None
    level_six: LevelSix | None
    tax_code: TaxCodeReferenceModel | None
    taxable_levels: list[int] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True