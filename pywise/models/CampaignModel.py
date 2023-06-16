from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CampaignTypeReferenceModel import CampaignTypeReferenceModel
from pywise.models.CampaignSubTypeReferenceModel import CampaignSubTypeReferenceModel
from pywise.models.CampaignStatusReferenceModel import CampaignStatusReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.GroupReferenceModel import GroupReferenceModel

class CampaignModel(ConnectWiseModel):
    id: int | None
    name: str | None
    type: CampaignTypeReferenceModel | None
    sub_type: CampaignSubTypeReferenceModel | None
    status: CampaignStatusReferenceModel | None
    start_date: str | None
    end_date: str | None
    location_id: int | None
    member: MemberReferenceModel | None
    inactive: bool | None
    inactive_days_after_end: int | None
    notes: str | None
    default_group: GroupReferenceModel | None
    marketing_manager_default_track_id: int | None
    opportunity_default_track_id: int | None
    impressions: int | None
    budget_revenue: float | None
    budget_cost: float | None
    actual_cost: float | None
    budget_gross_margin: float | None
    budget_r_o_i: float | None
    actual_revenue: float | None
    actual_gross_margin: float | None
    actual_r_o_i: float | None
    emails_sent: int | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True