from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from pywise.models.TicketReferenceModel import TicketReferenceModel
from pywise.models.SystemLocationReferenceModel import SystemLocationReferenceModel
from enum import Enum
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pywise.models.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pywise.models.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pywise.models.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pywise.models.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pywise.models.IvItemReferenceModel import IvItemReferenceModel
class BillingMethod(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'
class CommissionBasis(str, Enum):
    GrossProfit = 'GrossProfit'
    SalesAmount = 'SalesAmount'
class InvoiceOption(str, Enum):
    AllInvoices = 'AllInvoices'
    PaidInvoices = 'PaidInvoices'

class CommissionModel(ConnectWiseModel):
    id: int | None
    member: MemberReferenceModel | None
    commission_percent: float | None
    date_start: str | None
    date_end: str | None
    location: SystemLocationReferenceModel | None
    department: SystemDepartmentReferenceModel | None
    company: CompanyReferenceModel | None
    site: SiteReferenceModel | None
    agreement: AgreementReferenceModel | None
    project: ProjectReferenceModel | None
    service_board: BoardReferenceModel | None
    ticket: TicketReferenceModel | None
    territory: SystemLocationReferenceModel | None
    billing_method: BillingMethod | None
    service_type: ServiceTypeReferenceModel | None
    project_board: ProjectBoardReferenceModel | None
    project_type: ProjectTypeReferenceModel | None
    agreement_type: AgreementTypeReferenceModel | None
    number_of_months: int | None
    product_category: ProductCategoryReferenceModel | None
    product_sub_category: ProductSubCategoryReferenceModel | None
    item: IvItemReferenceModel | None
    commission_basis: CommissionBasis | None
    invoice_option: InvoiceOption | None
    services_flag: bool | None
    agreements_flag: bool | None
    products_flag: bool | None
    my_opportunities_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True