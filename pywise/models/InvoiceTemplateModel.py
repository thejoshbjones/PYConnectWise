from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class HeaderLogoPosition(str, Enum):
    Center = 'Center'
    LeftSide = 'LeftSide'
    RightSide = 'RightSide'
class HeaderAddressPosition(str, Enum):
    Center = 'Center'
    LeftSide = 'LeftSide'
    RightSide = 'RightSide'
class HeaderTitlePosition(str, Enum):
    Center = 'Center'
    LeftSide = 'LeftSide'
    RightSide = 'RightSide'
class HeaderTitleFont(str, Enum):
    Regular = 'Regular'
    RegularBold = 'RegularBold'
    Large = 'Large'
    LargeBold = 'LargeBold'
    ExtraLarge = 'ExtraLarge'
    ExtraLargeBold = 'ExtraLargeBold'

class InvoiceTemplateModel(ConnectWiseModel):
    id: int | None
    name: str | None
    margin_left: float | None
    margin_right: float | None
    margin_top: float | None
    margin_bottom: float | None
    logo_visible_flag: bool | None
    header_logo_position: HeaderLogoPosition | None
    remit_to_visible_flag: bool | None
    header_address_position: HeaderAddressPosition | None
    header_title_visible_flag: bool | None
    header_title_caption: str | None
    header_title_position: HeaderTitlePosition | None
    header_title_font: HeaderTitleFont | None
    header_terms_visible_flag: bool | None
    header_terms_caption: str | None
    header_due_date_visible_flag: bool | None
    header_due_date_caption: str | None
    header_po_number_visible_flag: bool | None
    header_po_number_caption: str | None
    header_reference_visible_flag: bool | None
    header_reference_caption: str | None
    header_account_visible_flag: bool | None
    header_account_caption: str | None
    header_tax_id_visible_flag: bool | None
    header_tax_id_caption: str | None
    header_ship_to_visible_flag: bool | None
    header_ship_to_caption: str | None
    header_hours_based_extended_amount_visible_flag: bool | None
    payable_caption: str | None
    service_header_ticket_number_visible_flag: bool | None
    service_header_ticket_number_caption: str | None
    service_header_company_name_visible_flag: bool | None
    service_header_company_name_caption: str | None
    service_header_summary_visible_flag: bool | None
    service_header_summary_caption: str | None
    service_header_contact_name_visible_flag: bool | None
    service_header_contact_name_caption: str | None
    service_header_detail_description_visible_flag: bool | None
    service_header_detail_description_caption: str | None
    service_header_resolution_visible_flag: bool | None
    service_header_resolution_caption: str | None
    service_header_amount_visible_flag: bool | None
    service_header_amount_caption: str | None
    service_header_billing_method_visible_flag: bool | None
    service_header_billing_method_caption: str | None
    service_header_closed_tasks_visible_flag: bool | None
    service_header_open_tasks_visible_flag: bool | None
    service_header_bundled_tickets_visible_flag: bool | None
    project_header_project_name_visible_flag: bool | None
    project_header_project_name_caption: str | None
    project_header_company_name_visible_flag: bool | None
    project_header_company_name_caption: str | None
    project_header_original_downpayment_visible_flag: bool | None
    project_header_original_downpayment_caption: str | None
    project_header_contact_name_visible_flag: bool | None
    project_header_contact_name_caption: str | None
    project_header_amount_visible_flag: bool | None
    project_header_amount_caption: str | None
    project_header_billing_method_visible_flag: bool | None
    project_header_billing_method_caption: str | None
    project_header_billing_type_visible_flag: bool | None
    project_header_billing_type_caption: str | None
    invoice_payment_amount_visible_flag: bool | None
    invoice_payment_amount_caption: str | None
    invoice_credit_amount_visible_flag: bool | None
    invoice_credit_amount_caption: str | None
    invoice_balance_due_visible_flag: bool | None
    invoice_balance_due_caption: str | None
    credit_credit_amount_visible_flag: bool | None
    credit_credit_amount_caption: str | None
    credit_remaining_amount_visible_flag: bool | None
    credit_remaining_amount_caption: str | None
    time_detail_visible_flag: bool | None
    time_detail_primary_sort_field: str | None
    time_detail_primary_sort_direction: str | None
    time_detail_secondary_sort_field: str | None
    time_detail_secondary_sort_direction: str | None
    time_detail_subtotal_visible_flag: bool | None
    time_detail_start_end_time_visible_flag: bool | None
    time_detail_hours_visible_flag: bool | None
    time_detail_members_visible_flag: bool | None
    time_detail_billable_visible_flag: bool | None
    time_detail_extended_amount_visible_flag: bool | None
    time_detail_dollar_amounts_on_hourse_based_visible_flag: bool | None
    time_detail_hourly_rate_visible_flag: bool | None
    time_detail_contacts_visible_flag: bool | None
    time_detail_notes_visible_flag: bool | None
    time_detail_non_billable_caption: str | None
    time_detail_agreement_visible_flag: bool | None
    time_detail_hours_based_hours_visible_flag: bool | None
    time_detail_hours_based_ext_amount_visible_flag: bool | None
    time_detail_hoursbased_hourly_rate_visible_flag: bool | None
    time_detail_amount_based_hours_visible_flag: bool | None
    time_detail_amount_based_ext_amount_visible_flag: bool | None
    time_detail_amount_based_hourly_rate_visible_flag: bool | None
    time_detail_s_r_ticket_summary_visible_flag: bool | None
    time_detail_s_r_contact_visible_flag: bool | None
    time_detail_s_r_address_visible_flag: bool | None
    time_detail_pm_phase_visible_flag: bool | None
    time_detail_pm_summary_visible_flag: bool | None
    time_detail_ticket_number_visible_flag: bool | None
    time_detail_dates_visible_flag: bool | None
    services_staff_caption: str | None
    services_staff_visible_flag: bool | None
    services_amount_caption: str | None
    services_amount_visible_flag: bool | None
    services_hours_caption: str | None
    services_hours_visible_flag: bool | None
    services_rate_caption: str | None
    services_rate_visible_flag: bool | None
    services_work_role_caption: str | None
    services_work_role_visible_flag: bool | None
    services_work_type_caption: str | None
    services_work_type_visible_flag: bool | None
    services_total_visible_flag: bool | None
    services_member_name_visible_flag: bool | None
    services_member_name_caption: str | None
    currency_id_visible_flag: bool | None
    currency_symbol_visible_flag: bool | None
    portal_flag: bool | None
    services_collapsed_flag: bool | None
    expenses_collapsed_flag: bool | None
    other_charges_collapsed_flag: bool | None
    expenses_type_caption: str | None
    expenses_staff_caption: str | None
    expenses_amount_caption: str | None
    expenses_type_visible_flag: bool | None
    expenses_staff_visible_flag: bool | None
    expenses_amount_visible_flag: bool | None
    expenses_total_visible_flag: bool | None
    expense_detail_subtotal_visible_flag: bool | None
    expense_detail_members_visible_flag: bool | None
    expense_detail_contacts_visible_flag: bool | None
    expense_detail_billable_visible_flag: bool | None
    expense_detail_ext_amount_visible_flag: bool | None
    expense_detail_notes_visible_flag: bool | None
    expense_detail_primary_sort_field: str | None
    expense_detail_primary_sort_direction: str | None
    expense_detail_secondary_sort_field: str | None
    expense_detail_secondary_sort_direction: str | None
    expense_detail_nonbillable_caption: str | None
    expense_detail_visible_flag: bool | None
    expense_detail_agreement_visible_flag: bool | None
    expense_detail_agreement_ext_amount_visible_flag: bool | None
    expense_detail_ticket_number_visible_flag: bool | None
    expense_detail_sr_ticket_summary_visible_flag: bool | None
    expense_detail_sr_contact_visible_flag: bool | None
    expense_detail_sr_address_visible_flag: bool | None
    expense_detail_pm_phase_visible_flag: bool | None
    expense_detail_pm_summary_visible_flag: bool | None
    other_charges_amount_caption: str | None
    other_charges_amount_visible_flag: bool | None
    other_charges_description_caption: str | None
    other_charges_description_visible_flag: bool | None
    other_charges_display_six_decimals: bool | None
    other_charges_item_id_visible_flag: bool | None
    other_charges_price_caption: str | None
    other_charges_price_visible_flag: bool | None
    other_charges_quantity_caption: str | None
    other_charges_quantity_visible_flag: bool | None
    other_charges_serial_number_visible_flag: bool | None
    other_charges_total_visible_flag: bool | None
    adjustment_description_visible_flag: bool | None
    adjustment_description_caption: str | None
    adjustment_quantity_visible_flag: bool | None
    adjustment_quantity_caption: str | None
    adjustment_amount_visible_flag: bool | None
    adjustment_amount_caption: str | None
    adjustment_agr_type_visible_flag: bool | None
    adjustment_total_visible_flag: bool | None
    adjustment_price_visible_flag: bool | None
    adjustment_price_caption: str | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True