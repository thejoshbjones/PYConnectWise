from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.DocumentReferenceModel import DocumentReferenceModel
from enum import Enum
class LicenseClass(str, Enum):
    A = 'A'
    C = 'C'
    F = 'F'
    X = 'X'

class MemberInfoModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    first_name: str | None
    middle_initial: str | None
    last_name: str | None
    full_name: str | None
    default_email: str | None
    photo: DocumentReferenceModel | None
    license_class: LicenseClass | None
    inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True