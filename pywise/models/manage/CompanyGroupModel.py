from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.GroupReferenceModel import GroupReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class CompanyGroupModel(ConnectWiseModel):
    id: int | None
    group: GroupReferenceModel | None
    company: CompanyReferenceModel | None
    default_contact_flag: bool | None
    all_contacts_flag: bool | None
    remove_all_contacts_flag: bool | None
    unsubscribe_flag: bool | None
    contact_ids: list[int] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True