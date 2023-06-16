from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel
from pywise.models.TicketReferenceModel import TicketReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.CampaignReferenceModel import CampaignReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.ScheduleStatusReferenceModel import ScheduleStatusReferenceModel
from pywise.models.ReminderReferenceModel import ReminderReferenceModel
from pywise.models.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel

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