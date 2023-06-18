from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

class DocumentInfoModel(ConnectWiseModel):
    id: int | None
    title: str | None
    file_name: str | None
    server_file_name: str | None
    owner: str | None
    link_flag: bool | None
    image_flag: bool | None
    public_flag: bool | None
    html_template_flag: bool | None
    read_only_flag: bool | None
    size: int | None
    url_flag: bool | None
    guid: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True