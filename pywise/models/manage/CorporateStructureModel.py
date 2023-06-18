from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
class LevelCount(str, Enum):
    Level1 = 'Level1'
    Level2 = 'Level2'
    Level3 = 'Level3'
    Level4 = 'Level4'
    Level5 = 'Level5'
class FiscalYearStart(str, Enum):
    January = 'January'
    February = 'February'
    March = 'March'
    April = 'April'
    May = 'May'
    June = 'June'
    July = 'July'
    August = 'August'
    September = 'September'
    October = 'October'
    November = 'November'
    December = 'December'

class CorporateStructureModel(ConnectWiseModel):
    id: int | None
    level_count: LevelCount | None
    level1_name: str | None
    level2_name: str | None
    level3_name: str | None
    level4_name: str | None
    level5_name: str | None
    fiscal_year_start: FiscalYearStart | None
    location_caption: str | None
    group_caption: str | None
    base_currency: CurrencyReferenceModel | None
    president: MemberReferenceModel | None
    chief_operating_officer: MemberReferenceModel | None
    controller: MemberReferenceModel | None
    dispatcher: MemberReferenceModel | None
    service_manager: MemberReferenceModel | None
    duty_manager: MemberReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True