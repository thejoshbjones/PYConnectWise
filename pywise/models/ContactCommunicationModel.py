from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CommunicationTypeReferenceModel import CommunicationTypeReferenceModel
from enum import Enum
class CommunicationType(str, Enum):
    Email = 'Email'
    Fax = 'Fax'
    Phone = 'Phone'

class ContactCommunicationModel(ConnectWiseModel):
    id: int | None
    contact_id: int | None
    type: CommunicationTypeReferenceModel | None
    value: str | None
    extension: str | None
    default_flag: bool | None
    mobile_guid: str | None
    communication_type: CommunicationType | None
    domain: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True