from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.ImapSetupReferenceModel import ImapSetupReferenceModel
from pywise.models.Office365EmailSetupReferenceModel import Office365EmailSetupReferenceModel
from pywise.models.GoogleEmailSetupReferenceModel import GoogleEmailSetupReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pywise.models.PriorityReferenceModel import PriorityReferenceModel
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.ServiceStatusReferenceModel import ServiceStatusReferenceModel
class EmailServerType(str, Enum):
    IMAP = 'IMAP'
    Office365 = 'Office365'
    Google = 'Google'

class EmailConnectorModel(ConnectWiseModel):
    id: int | None
    email_server_type: EmailServerType | None
    imap_setup: ImapSetupReferenceModel | None
    office365_email_setup: Office365EmailSetupReferenceModel | None
    google_email_setup: GoogleEmailSetupReferenceModel | None
    service_board: BoardReferenceModel | None
    default_company: CompanyReferenceModel | None
    default_member: MemberReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    email_notify_from: str | None
    bcc_email_to: str | None
    email_errors_to: str | None
    set_email_to_default_contact_flag: bool | None
    no_response_flag: bool | None
    never_respond_flag: bool | None
    discard_duplicates_flag: bool | None
    post_replies_to_ticket_flag: bool | None
    create_contact_flag: bool | None
    response_email_for_new: str | None
    response_email_for_existing: str | None
    source_override: ServiceSourceReferenceModel | None
    priority_override: PriorityReferenceModel | None
    type_override: ServiceTypeReferenceModel | None
    sub_type_override: ServiceSubTypeReferenceModel | None
    item_override: ServiceItemReferenceModel | None
    status_override: ServiceStatusReferenceModel | None
    add_cc_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True