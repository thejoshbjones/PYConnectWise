from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.CountryReferenceModel import CountryReferenceModel
from enum import Enum
class LevelOneRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelTwoRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelThreeRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelFourRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelFiveRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelSixRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'

class TaxCodeModel(ConnectWiseModel):
    id: int | None
    identifier: str | None
    description: str | None
    invoice_caption: str | None
    country: CountryReferenceModel | None
    effective_date: str | None
    default_flag: bool | None
    display_on_invoice_flag: bool | None
    canada_calculate_g_s_t_flag: bool | None
    cancel_date: str | None
    level_one_rate: float | None
    level_one_rate_type: LevelOneRateType | None
    level_one_taxable_max: float | None
    level_one_caption: str | None
    level_one_tax_code_xref: str | None
    level_one_agency_xref: str | None
    level_one_services_flag: bool | None
    level_one_expenses_flag: bool | None
    level_one_products_flag: bool | None
    level_one_apply_single_unit_flag: bool | None
    level_one_apply_single_unit_min: float | None
    level_one_apply_single_unit_max: float | None
    level_two_rate: float | None
    level_two_rate_type: LevelTwoRateType | None
    level_two_taxable_max: float | None
    level_two_caption: str | None
    level_two_tax_code_xref: str | None
    level_two_agency_xref: str | None
    level_two_services_flag: bool | None
    level_two_expenses_flag: bool | None
    level_two_products_flag: bool | None
    level_two_apply_single_unit_flag: bool | None
    level_two_apply_single_unit_min: float | None
    level_two_apply_single_unit_max: float | None
    level_three_rate: float | None
    level_three_rate_type: LevelThreeRateType | None
    level_three_taxable_max: float | None
    level_three_caption: str | None
    level_three_tax_code_xref: str | None
    level_three_agency_xref: str | None
    level_three_services_flag: bool | None
    level_three_expenses_flag: bool | None
    level_three_products_flag: bool | None
    level_three_apply_single_unit_flag: bool | None
    level_three_apply_single_unit_min: float | None
    level_three_apply_single_unit_max: float | None
    level_four_rate: float | None
    level_four_rate_type: LevelFourRateType | None
    level_four_taxable_max: float | None
    level_four_caption: str | None
    level_four_tax_code_xref: str | None
    level_four_agency_xref: str | None
    level_four_services_flag: bool | None
    level_four_expenses_flag: bool | None
    level_four_products_flag: bool | None
    level_four_apply_single_unit_flag: bool | None
    level_four_apply_single_unit_min: float | None
    level_four_apply_single_unit_max: float | None
    level_five_rate: float | None
    level_five_rate_type: LevelFiveRateType | None
    level_five_taxable_max: float | None
    level_five_caption: str | None
    level_five_tax_code_xref: str | None
    level_five_agency_xref: str | None
    level_five_services_flag: bool | None
    level_five_expenses_flag: bool | None
    level_five_products_flag: bool | None
    level_five_apply_single_unit_flag: bool | None
    level_five_apply_single_unit_min: float | None
    level_five_apply_single_unit_max: float | None
    level_six_rate: float | None
    level_six_rate_type: LevelSixRateType | None
    level_six_taxable_max: float | None
    level_six_caption: str | None
    level_six_tax_code_xref: str | None
    level_six_agency_xref: str | None
    level_six_services_flag: bool | None
    level_six_expenses_flag: bool | None
    level_six_products_flag: bool | None
    level_six_apply_single_unit_flag: bool | None
    level_six_apply_single_unit_min: float | None
    level_six_apply_single_unit_max: float | None
    work_role_ids: list[int] | None
    add_all_work_roles: bool | None
    remove_all_work_roles: bool | None
    expense_type_ids: list[int] | None
    add_all_expense_types: bool | None
    remove_all_expense_types: bool | None
    product_type_ids: list[int] | None
    add_all_product_types: bool | None
    remove_all_product_types: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True