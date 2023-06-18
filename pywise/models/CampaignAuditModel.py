from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.GroupReferenceModel import GroupReferenceModel

class CampaignAuditModel(ConnectWiseModel):
    id: int | None
    emails_sent: int | None
    emails_unsent: int | None
    documents_created: int | None
    email_subject: str | None
    group: GroupReferenceModel | None
    campaign_id: int | None
    created_by: str | None
    date_created: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True