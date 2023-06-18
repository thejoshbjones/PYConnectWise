from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.WorkRoleReferenceModel import WorkRoleReferenceModel

class AgreementTypeWorkRoleInfoModel(ConnectWiseModel):
    id: int | None
    type: AgreementTypeReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True