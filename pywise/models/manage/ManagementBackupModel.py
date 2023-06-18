from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from enum import Enum
class BillingLevel(str, Enum):
    Detail = 'Detail'
    Summary = 'Summary'

class ManagementBackupModel(ConnectWiseModel):
    id: int | None
    type: AgreementTypeReferenceModel | None
    item: CatalogItemReferenceModel | None
    billing_level: BillingLevel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True