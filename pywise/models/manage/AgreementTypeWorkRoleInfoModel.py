from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class AgreementTypeWorkRoleInfoModel(ConnectWiseModel):
    id: int
    type: AgreementTypeReferenceModel
    work_role: WorkRoleReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True