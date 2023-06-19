from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CorporateStructureLevelReferenceModel import CorporateStructureLevelReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel

class LocationModel(ConnectWiseModel):
    id: int
    owner_level_id: int
    structure_level: CorporateStructureLevelReferenceModel
    name: str
    manager: MemberReferenceModel
    reports_to: SystemLocationReferenceModel
    sales_rep: str
    time_zone_setup: TimeZoneSetupReferenceModel
    calendar: CalendarReferenceModel
    override_address_line1: str
    override_address_line2: str
    override_city: str
    override_state: str
    override_zip: str
    override_country: CountryReferenceModel
    override_phone_number: str
    override_fax_number: str
    owa_url: str
    payroll_xref: str
    location_flag: bool
    client_flag: bool
    work_role_ids: list[int]
    department_ids: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True