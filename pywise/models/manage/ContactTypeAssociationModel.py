from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.ContactTypeReferenceModel import ContactTypeReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel

class ContactTypeAssociationModel(ConnectWiseModel):
    id: int
    type: ContactTypeReferenceModel
    contact: ContactReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True