from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pywise.models.PurchaseOrderStatusReferenceModel import PurchaseOrderStatusReferenceModel
from pywise.models.TaxCodeReferenceModel import TaxCodeReferenceModel
from pywise.models.BillingTermsReferenceModel import BillingTermsReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.WarehouseReferenceModel import WarehouseReferenceModel
from pywise.models.CurrencyReferenceModel import CurrencyReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel

class PurchaseOrderModel(ConnectWiseModel):
    id: int | None
    business_unit_id: int | None
    cancel_reason: str | None
    closed_flag: bool | None
    customer_city: str | None
    customer_company: CompanyReferenceModel | None
    customer_contact: ContactReferenceModel | None
    customer_country: CountryReferenceModel | None
    customer_extension: str | None
    customer_name: str | None
    customer_phone: str | None
    customer_site: SiteReferenceModel | None
    customer_site_name: str | None
    customer_state: str | None
    customer_street_line1: str | None
    customer_street_line2: str | None
    customer_zip: str | None
    date_closed: str | None
    drop_ship_customer_flag: bool | None
    entered_by: str | None
    freight_cost: float | None
    freight_packing_slip: str | None
    freight_tax_total: float | None
    internal_notes: str | None
    location_id: int | None
    po_date: str | None
    po_number: str | None
    sales_tax: float | None
    shipment_date: str | None
    shipment_method: ShipmentMethodReferenceModel | None
    shipping_instructions: str | None
    status: PurchaseOrderStatusReferenceModel | None
    sub_total: float | None
    tax_code: TaxCodeReferenceModel | None
    tax_freight_flag: bool | None
    tax_po_flag: bool | None
    terms: BillingTermsReferenceModel | None
    total: float | None
    tracking_number: str | None
    update_shipment_info: bool | None
    update_vendor_order_number: bool | None
    vendor_company: CompanyReferenceModel | None
    vendor_contact: ContactReferenceModel | None
    vendor_invoice_date: str | None
    vendor_invoice_number: str | None
    vendor_order_number: str | None
    vendor_site: SiteReferenceModel | None
    warehouse: WarehouseReferenceModel | None
    currency: CurrencyReferenceModel | None
    _info: dict[str, str] | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True