from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pywise.models.MappedTypeReferenceModel import MappedTypeReferenceModel
from pywise.models.MappedRecordReferenceModel import MappedRecordReferenceModel
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

class GLAccountModel(ConnectWiseModel):
    id: int | None
    gl_type: GlType | None
    mapped_type: MappedTypeReferenceModel | None
    mapped_record: MappedRecordReferenceModel | None
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
    product_id: str | None
    inventory: str | None
    sales_code: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True