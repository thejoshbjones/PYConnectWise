from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.manage.UserDefinedFieldOptionModel import UserDefinedFieldOptionModel
class FieldTypeIdentifier(str, Enum):
    TextArea = 'TextArea'
    Button = 'Button'
    Currency = 'Currency'
    Date = 'Date'
    Hyperlink = 'Hyperlink'
    IPAddress = 'IPAddress'
    Checkbox = 'Checkbox'
    Number = 'Number'
    Percent = 'Percent'
    Text = 'Text'
    Password = 'Password'
class EntryTypeIdentifier(str, Enum):
    Date = 'Date'
    EntryField = 'EntryField'
    List = 'List'
    Option = 'Option'

class UserDefinedFieldInfoModel(ConnectWiseModel):
    id: int | None
    pod_id: int | None
    caption: str | None
    sequence_number: int | None
    help_text: str | None
    field_type_identifier: FieldTypeIdentifier | None
    number_decimals: int | None
    entry_type_identifier: EntryTypeIdentifier | None
    required_flag: bool | None
    display_on_screen_flag: bool | None
    read_only_flag: bool | None
    list_view_flag: bool | None
    button_url: str | None
    options: list[UserDefinedFieldOptionModel] | None
    business_unit_ids: list[int] | None
    location_ids: list[int] | None
    date_created: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True