from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class AuditTrailEntryModel(ConnectWiseModel):
    text: str | None
    entered_date: str | None
    entered_by: str | None
    audit_type: str | None
    audit_sub_type: str | None
    audit_source: str | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True