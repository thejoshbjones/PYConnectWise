from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.TicketReferenceModel import TicketReferenceModel
from pywise.models.manage.SalesOrderReferenceModel import SalesOrderReferenceModel
from pywise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pywise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pywise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pywise.models.manage.RmaStatusReferenceModel import RmaStatusReferenceModel
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.RmaDispositionReferenceModel import RmaDispositionReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.RmaActionReferenceModel import RmaActionReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.MemberReferenceModel import MemberReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class RmaTagModel(ConnectWiseModel):
    id: int
    service_ticket: TicketReferenceModel
    sales_order: SalesOrderReferenceModel
    invoice: InvoiceReferenceModel
    project: ProjectReferenceModel
    summary: str
    product: IvItemReferenceModel
    iv_description: str
    product_description: str
    serial_number: str
    mfg_item_i_d: str
    status: RmaStatusReferenceModel
    list_price: float
    unit_price: float
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    problem_description: str
    returned_company: CompanyReferenceModel
    returned_contact: ContactReferenceModel
    returned_contact_type: str
    returned_contact_phone: str
    returned_contact_extension: str
    returned_contact_email: str
    returned_contact_address_line1: str
    returned_contact_address_line2: str
    returned_contact_city: str
    returned_contact_state: str
    returned_contact_zip: str
    returned_contact_country: CountryReferenceModel
    rma_disposition: RmaDispositionReferenceModel
    returned_site: SiteReferenceModel
    purchased_company: CompanyReferenceModel
    purchased_contact: ContactReferenceModel
    purchased_contact_type: str
    purchased_contact_phone: str
    purchased_contact_extension: str
    purchased_contact_email: str
    purchased_contact_address_line1: str
    purchased_contact_address_line2: str
    purchased_contact_city: str
    purchased_contact_state: str
    purchased_contact_zip: str
    purchased_contact_country: CountryReferenceModel
    purchased_invoice_number: str
    purchased_invoice_date: str
    purchased_order_number: str
    purchased_vendor_action: RmaActionReferenceModel
    purchased_vendor_rma_number: str
    purchased_site: SiteReferenceModel
    purchased_notes: str
    warranty_company: CompanyReferenceModel
    warranty_contact: ContactReferenceModel
    warranty_contact_type: str
    warranty_contact_phone: str
    warranty_contact_email: str
    warranty_contact_extension: str
    warranty_contact_address_line1: str
    warranty_contact_address_line2: str
    warranty_contact_city: str
    warranty_contact_state: str
    warranty_contact_zip: str
    warranty_contact_country: CountryReferenceModel
    warranty_site: SiteReferenceModel
    warranty_notes: str
    repair_company: CompanyReferenceModel
    repair_contact: ContactReferenceModel
    repair_contact_type: str
    repair_contact_phone: str
    repair_contact_extension: str
    repair_contact_email: str
    repair_contact_address_line1: str
    repair_contact_address_line2: str
    repair_contact_city: str
    repair_contact_state: str
    repair_contact_zip: str
    repair_contact_country: CountryReferenceModel
    repair_order_number: str
    repair_site: SiteReferenceModel
    repair_notes: str
    drop_ship_flag: bool
    ship_method: ShipmentMethodReferenceModel
    shipping_date: str
    shipping_tracking_number: str
    internal_notes: str
    closing_notes: str
    date_closed: str
    account_manager: MemberReferenceModel
    technical_contact: MemberReferenceModel
    currency: CurrencyReferenceModel
    closed_by: MemberReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True