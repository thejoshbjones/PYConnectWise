from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.GroupReferenceModel import GroupReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel

class ContactGroupModel(ConnectWiseModel):
    id: int | None
    group: GroupReferenceModel | None
    contact: ContactReferenceModel | None
    description: str | None
    unsubscribe_flag: bool | None
    company_unsubcribed_email_message: str | None
    company_group_unsubscribed_email_message: str | None
    contact_unsubscribed_email_message: str | None
    contact_group_unsubscribed_email_message: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True