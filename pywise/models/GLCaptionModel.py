from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Segment1type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment2type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment3type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment4type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment5type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment6type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment7type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment8type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment9type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment10type(str, Enum):
    Account = 'Account'
    Class = 'Class'

class GLCaptionModel(ConnectWiseModel):
    id: int | None
    segment1: str | None
    segment2: str | None
    segment3: str | None
    segment4: str | None
    segment5: str | None
    segment6: str | None
    segment7: str | None
    segment8: str | None
    segment9: str | None
    segment10: str | None
    segment1type: Segment1type | None
    segment2type: Segment2type | None
    segment3type: Segment3type | None
    segment4type: Segment4type | None
    segment5type: Segment5type | None
    segment6type: Segment6type | None
    segment7type: Segment7type | None
    segment8type: Segment8type | None
    segment9type: Segment9type | None
    segment10type: Segment10type | None
    cogs1: str | None
    cogs2: str | None
    cogs3: str | None
    cogs4: str | None
    cogs5: str | None
    cogs6: str | None
    cogs7: str | None
    cogs8: str | None
    cogs9: str | None
    cogs10: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True