from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
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

class ConfigurationQuestionModel(ConnectWiseModel):
    answer_id: int | None
    question_id: int | None
    question: str | None
    answer: dict[str, Any] | None
    sequence_number: float | None
    number_of_decimals: int | None
    field_type: FieldType | None
    required_flag: bool | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True