from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.StateReferenceModel import StateReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.EntityTypeReferenceModel import EntityTypeReferenceModel
from pywise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class CompanySiteModel(ConnectWiseModel):
    id: int | None
    name: str | None
    address_line1: str | None
    address_line2: str | None
    city: str | None
    state_reference: StateReferenceModel | None
    zip: str | None
    country: CountryReferenceModel | None
    address_format: str | None
    phone_number: str | None
    fax_number: str | None
    tax_code: TaxCodeReferenceModel | None
    entity_type: EntityTypeReferenceModel | None
    expense_reimbursement: float | None
    primary_address_flag: bool | None
    default_shipping_flag: bool | None
    default_billing_flag: bool | None
    default_mailing_flag: bool | None
    inactive_flag: bool | None
    bill_separate_flag: bool | None
    mobile_guid: str | None
    calendar: CalendarReferenceModel | None
    time_zone: TimeZoneSetupReferenceModel | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True