from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.KBCategoryReferenceModel import KBCategoryReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel

class KnowledgeBaseSubCategoryModel(ConnectWiseModel):
    id: int | None
    name: str | None
    category: KBCategoryReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True