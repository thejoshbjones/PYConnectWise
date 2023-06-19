from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.GroupReferenceModel import GroupReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class CompanyGroupModel(ConnectWiseModel):
    id: int
    group: GroupReferenceModel
    company: CompanyReferenceModel
    default_contact_flag: bool
    all_contacts_flag: bool
    remove_all_contacts_flag: bool
    unsubscribe_flag: bool
    contact_ids: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True