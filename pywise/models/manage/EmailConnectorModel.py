from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.ImapSetupReferenceModel import ImapSetupReferenceModel
from pywise.models.manage.Office365EmailSetupReferenceModel import Office365EmailSetupReferenceModel
from pywise.models.manage.GoogleEmailSetupReferenceModel import GoogleEmailSetupReferenceModel
from pywise.models.manage.BoardReferenceModel import BoardReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
class EmailServerType(str, Enum):
    IMAP = 'IMAP'
    Office365 = 'Office365'
    Google = 'Google'

class EmailConnectorModel(ConnectWiseModel):
    id: int
    email_server_type: EmailServerType
    imap_setup: ImapSetupReferenceModel
    office365_email_setup: Office365EmailSetupReferenceModel
    google_email_setup: GoogleEmailSetupReferenceModel
    service_board: BoardReferenceModel
    default_company: CompanyReferenceModel
    default_member: MemberReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    email_notify_from: str
    bcc_email_to: str
    email_errors_to: str
    set_email_to_default_contact_flag: bool
    no_response_flag: bool
    never_respond_flag: bool
    discard_duplicates_flag: bool
    post_replies_to_ticket_flag: bool
    create_contact_flag: bool
    response_email_for_new: str
    response_email_for_existing: str
    source_override: ServiceSourceReferenceModel
    priority_override: PriorityReferenceModel
    type_override: ServiceTypeReferenceModel
    sub_type_override: ServiceSubTypeReferenceModel
    item_override: ServiceItemReferenceModel
    status_override: ServiceStatusReferenceModel
    add_cc_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True