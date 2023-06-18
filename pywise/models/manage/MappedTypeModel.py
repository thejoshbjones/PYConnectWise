from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class GlType(str, Enum):
    AP = 'AP'
    AR = 'AR'
    EE = 'EE'
    EI = 'EI'
    EO = 'EO'
    IA = 'IA'
    IT = 'IT'
    P = 'P'
    PF = 'PF'
    R = 'R'
    RA = 'RA'
    RD = 'RD'
    RE = 'RE'
    RP = 'RP'
    ST = 'ST'
    SD = 'SD'
    ET = 'ET'
    FT = 'FT'
    PT = 'PT'

class MappedTypeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    table: str | None
    rec_id_field: str | None
    gl_type: GlType | None
    sort_order: int | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True