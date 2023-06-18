from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from enum import Enum
from pywise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pywise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'

class ChargeCodeModel(ConnectWiseModel):
    id: int | None
    name: str | None
    company: CompanyReferenceModel | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    bill_time: BillTime | None
    expense_entry_flag: bool | None
    allow_all_expense_type_flag: bool | None
    time_entry_flag: bool | None
    work_type: WorkTypeReferenceModel | None
    work_role: WorkRoleReferenceModel | None
    integration_xref: str | None
    expense_type_ids: list[int] | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True