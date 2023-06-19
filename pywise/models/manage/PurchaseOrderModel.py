from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.manage.PurchaseOrderStatusReferenceModel import PurchaseOrderStatusReferenceModel
from pywise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class PurchaseOrderModel(ConnectWiseModel):
    id: int
    business_unit_id: int
    cancel_reason: str
    closed_flag: bool
    customer_city: str
    customer_company: CompanyReferenceModel
    customer_contact: ContactReferenceModel
    customer_country: CountryReferenceModel
    customer_extension: str
    customer_name: str
    customer_phone: str
    customer_site: SiteReferenceModel
    customer_site_name: str
    customer_state: str
    customer_street_line1: str
    customer_street_line2: str
    customer_zip: str
    date_closed: str
    drop_ship_customer_flag: bool
    entered_by: str
    freight_cost: float
    freight_packing_slip: str
    freight_tax_total: float
    internal_notes: str
    location_id: int
    po_date: str
    po_number: str
    sales_tax: float
    shipment_date: str
    shipment_method: ShipmentMethodReferenceModel
    shipping_instructions: str
    status: PurchaseOrderStatusReferenceModel
    sub_total: float
    tax_code: TaxCodeReferenceModel
    tax_freight_flag: bool
    tax_po_flag: bool
    terms: BillingTermsReferenceModel
    total: float
    tracking_number: str
    update_shipment_info: bool
    update_vendor_order_number: bool
    vendor_company: CompanyReferenceModel
    vendor_contact: ContactReferenceModel
    vendor_invoice_date: str
    vendor_invoice_number: str
    vendor_order_number: str
    vendor_site: SiteReferenceModel
    warehouse: WarehouseReferenceModel
    currency: CurrencyReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True