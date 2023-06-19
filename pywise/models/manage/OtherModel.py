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
    id: int
    default_ldap: LdapConfigurationReferenceModel
    default_from_address: str
    portal_url_override: str
    site_url: str
    logo_path: str
    contact_sync: ContactSync
    server_time_zone: TimeZoneSetupReferenceModel
    default_calendar: CalendarReferenceModel
    default_address_format: AddressFormatReferenceModel
    use_ssl_flag: bool
    sync_leads_flag: bool
    include_portal_link_flag: bool
    use_expanded_format_time_flag: bool
    use_expanded_format_activity_flag: bool
    disable_z_admin_login_flag: bool
    locale: LocaleReferenceModel
    update_member_time_zones_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True