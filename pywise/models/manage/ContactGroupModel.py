from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.GroupReferenceModel import GroupReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel

class ContactGroupModel(ConnectWiseModel):
    id: int
    group: GroupReferenceModel
    contact: ContactReferenceModel
    description: str
    unsubscribe_flag: bool
    company_unsubcribed_email_message: str
    company_group_unsubscribed_email_message: str
    contact_unsubscribed_email_message: str
    contact_group_unsubscribed_email_message: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True