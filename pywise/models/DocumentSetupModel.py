from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class DocumentSetupModel(ConnectWiseModel):
    id: int | None
    upload_as_link_flag: bool | None
    is_public_flag: bool | None
    doc_path: str | None
    template_path: str | None
    template_output_path: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True