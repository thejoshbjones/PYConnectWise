from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CorporateStructureLevelReferenceModel import CorporateStructureLevelReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel

class LocationModel(ConnectWiseModel):
    id: int | None
    owner_level_id: int | None
    structure_level: CorporateStructureLevelReferenceModel | None
    name: str | None
    manager: MemberReferenceModel | None
    reports_to: SystemLocationReferenceModel | None
    sales_rep: str | None
    time_zone_setup: TimeZoneSetupReferenceModel | None
    calendar: CalendarReferenceModel | None
    override_address_line1: str | None
    override_address_line2: str | None
    override_city: str | None
    override_state: str | None
    override_zip: str | None
    override_country: CountryReferenceModel | None
    override_phone_number: str | None
    override_fax_number: str | None
    owa_url: str | None
    payroll_xref: str | None
    location_flag: bool | None
    client_flag: bool | None
    work_role_ids: list[int] | None
    department_ids: list[int] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True