from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pywise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.CampaignReferenceModel import CampaignReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ScheduleStatusReferenceModel import ScheduleStatusReferenceModel
from pywise.models.manage.ReminderReferenceModel import ReminderReferenceModel
from pywise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class ActivityModel(ConnectWiseModel):
    id: int
    name: str
    type: ActivityTypeReferenceModel
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    phone_number: str
    email: str
    status: ActivityStatusReferenceModel
    opportunity: OpportunityReferenceModel
    ticket: TicketReferenceModel
    agreement: AgreementReferenceModel
    campaign: CampaignReferenceModel
    notes: str
    date_start: str
    date_end: str
    assigned_by: MemberReferenceModel
    assign_to: MemberReferenceModel
    schedule_status: ScheduleStatusReferenceModel
    reminder: ReminderReferenceModel
    where: ServiceLocationReferenceModel
    notify_flag: bool
    mobile_guid: str
    currency: CurrencyReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True