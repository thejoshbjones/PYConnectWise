from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class DocumentSetupModel(ConnectWiseModel):
    id: int
    upload_as_link_flag: bool
    is_public_flag: bool
    doc_path: str
    template_path: str
    template_output_path: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True