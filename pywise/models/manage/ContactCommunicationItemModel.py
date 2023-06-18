from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CommunicationTypeReferenceModel import CommunicationTypeReferenceModel
from enum import Enum
class CommunicationType(str, Enum):
    Email = 'Email'
    Fax = 'Fax'
    Phone = 'Phone'

class ContactCommunicationItemModel(ConnectWiseModel):
    id: int | None
    type: CommunicationTypeReferenceModel | None
    value: str | None
    extension: str | None
    default_flag: bool | None
    domain: str | None
    communication_type: CommunicationType | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True