from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.KPIReferenceModel import KPIReferenceModel
from pywise.models.manage.ReportCardReferenceModel import ReportCardReferenceModel

class ReportCardDetailModel(ConnectWiseModel):
    id: int | None
    kpi: KPIReferenceModel | None
    sort_order: int | None
    report_card: ReportCardReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True