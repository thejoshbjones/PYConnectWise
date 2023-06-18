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
    id: int | None
    name: str | None
    type: ActivityTypeReferenceModel | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    phone_number: str | None
    email: str | None
    status: ActivityStatusReferenceModel | None
    opportunity: OpportunityReferenceModel | None
    ticket: TicketReferenceModel | None
    agreement: AgreementReferenceModel | None
    campaign: CampaignReferenceModel | None
    notes: str | None
    date_start: str | None
    date_end: str | None
    assigned_by: MemberReferenceModel | None
    assign_to: MemberReferenceModel | None
    schedule_status: ScheduleStatusReferenceModel | None
    reminder: ReminderReferenceModel | None
    where: ServiceLocationReferenceModel | None
    notify_flag: bool | None
    mobile_guid: str | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True