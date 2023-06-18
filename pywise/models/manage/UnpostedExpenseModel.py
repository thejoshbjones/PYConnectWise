from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel
from enum import Enum
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.ChargeCodeReferenceModel import ChargeCodeReferenceModel
from pywise.models.manage.PaymentMethodReferenceModel import PaymentMethodReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
class Classification(str, Enum):
    NonReimbursable = 'NonReimbursable'
    Reimbursable = 'Reimbursable'
    Personal = 'Personal'
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

class UnpostedExpenseModel(ConnectWiseModel):
    id: int | None
    location_id: int | None
    department_id: int | None
    company: CompanyReferenceModel | None
    account_number: str | None
    credit_account: str | None
    expense_detail_id: int | None
    expense_type: ExpenseTypeReferenceModel | None
    classification: Classification | None
    gl_type: GlType | None
    member: MemberReferenceModel | None
    date_expense: str | None
    charge_code: ChargeCodeReferenceModel | None
    charge_description: str | None
    in_policy: bool | None
    payment_method: PaymentMethodReferenceModel | None
    currency: CurrencyReferenceModel | None
    total: float | None
    billable_amount: float | None
    non_billable_amount: float | None
    agreement: AgreementReferenceModel | None
    agreement_amount_covered: float | None
    ticket: TicketReferenceModel | None
    project: ProjectReferenceModel | None
    project_phase: ProjectPhaseReferenceModel | None
    tax_code: TaxCodeReferenceModel | None
    avalara_tax_flag: bool | None
    item_taxable_flag: bool | None
    sales_tax_amount: float | None
    state_tax_flag: bool | None
    state_tax_xref: str | None
    state_tax_amount: float | None
    county_tax_flag: bool | None
    county_tax_xref: str | None
    county_tax_amount: float | None
    city_tax_flag: bool | None
    city_tax_xref: str | None
    city_tax_amount: float | None
    country_tax_flag: bool | None
    country_tax_xref: str | None
    country_tax_amount: float | None
    composite_tax_flag: bool | None
    composite_tax_xref: str | None
    composite_tax_amount: float | None
    level_six_tax_flag: bool | None
    level_six_tax_xref: str | None
    level_six_tax_amount: float | None
    date_closed: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True