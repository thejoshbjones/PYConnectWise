from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel
from enum import Enum
class FieldType(str, Enum):
    TextArea = 'TextArea'
    Currency = 'Currency'
    Date = 'Date'
    Hyperlink = 'Hyperlink'
    IPAddress = 'IPAddress'
    Checkbox = 'Checkbox'
    Number = 'Number'
    Percent = 'Percent'
    Text = 'Text'
    Password = 'Password'
class EntryType(str, Enum):
    Date = 'Date'
    EntryField = 'EntryField'
    List = 'List'
    Option = 'Option'

class ConfigurationTypeQuestionModel(ConnectWiseModel):
    id: int | None
    configuration_type: ConfigurationTypeReferenceModel | None
    field_type: FieldType | None
    entry_type: EntryType | None
    sequence_number: float | None
    question: str | None
    number_of_decimals: int | None
    required_flag: bool | None
    inactive_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True