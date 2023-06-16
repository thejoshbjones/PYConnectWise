from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class CustomFieldValueModelType(str, Enum):
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
class EntryMethod(str, Enum):
    Date = 'Date'
    EntryField = 'EntryField'
    List = 'List'
    Option = 'Option'

class CustomFieldValueModel(ConnectWiseModel):
    id: int | None
    caption: str | None
    type: CustomFieldValueModelType | None
    entry_method: EntryMethod | None
    number_of_decimals: int | None
    value: dict[str, Any] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True