from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class ImportMassMaintenanceModel(ConnectWiseModel):
    deleted_contact_count: int | None
    deleted_company_count: int | None
    message: str | None
    success: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True