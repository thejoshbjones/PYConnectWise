from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.LdapConfigurationReferenceModel import LdapConfigurationReferenceModel
from enum import Enum
from pywise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pywise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pywise.models.manage.AddressFormatReferenceModel import AddressFormatReferenceModel
from pywise.models.manage.LocaleReferenceModel import LocaleReferenceModel
class ContactSync(str, Enum):
    FL = 'FL'
    LF = 'LF'
    CFL = 'CFL'
    CLF = 'CLF'

class OtherModel(ConnectWiseModel):
    id: int | None
    default_ldap: LdapConfigurationReferenceModel | None
    default_from_address: str | None
    portal_url_override: str | None
    site_url: str | None
    logo_path: str | None
    contact_sync: ContactSync | None
    server_time_zone: TimeZoneSetupReferenceModel | None
    default_calendar: CalendarReferenceModel | None
    default_address_format: AddressFormatReferenceModel | None
    use_ssl_flag: bool | None
    sync_leads_flag: bool | None
    include_portal_link_flag: bool | None
    use_expanded_format_time_flag: bool | None
    use_expanded_format_activity_flag: bool | None
    disable_z_admin_login_flag: bool | None
    locale: LocaleReferenceModel | None
    update_member_time_zones_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True