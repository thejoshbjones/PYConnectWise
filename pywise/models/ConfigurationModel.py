from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel
from pywise.models.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ContactReferenceModel import ContactReferenceModel
from pywise.models.SiteReferenceModel import SiteReferenceModel
from pywise.models.MemberReferenceModel import MemberReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.ManufacturerReferenceModel import ManufacturerReferenceModel
from pywise.models.ConfigurationQuestionModel import ConfigurationQuestionModel
from pywise.models.SLAReferenceModel import SLAReferenceModel
from pywise.models.CustomFieldValueModel import CustomFieldValueModel

class ConfigurationModel(ConnectWiseModel):
    id: int | None
    name: str | None
    type: ConfigurationTypeReferenceModel | None
    status: ConfigurationStatusReferenceModel | None
    company: CompanyReferenceModel | None
    contact: ContactReferenceModel | None
    site: SiteReferenceModel | None
    location_id: int | None
    business_unit_id: int | None
    device_identifier: str | None
    serial_number: str | None
    model_number: str | None
    tag_number: str | None
    purchase_date: str | None
    installation_date: str | None
    installed_by: MemberReferenceModel | None
    warranty_expiration_date: str | None
    vendor_notes: str | None
    notes: str | None
    mac_address: str | None
    last_login_name: str | None
    bill_flag: bool | None
    backup_successes: int | None
    backup_incomplete: int | None
    backup_failed: int | None
    backup_restores: int | None
    last_backup_date: str | None
    backup_server_name: str | None
    backup_billable_space_gb: float | None
    backup_protected_device_list: str | None
    backup_year: int | None
    backup_month: int | None
    ip_address: str | None
    default_gateway: str | None
    os_type: str | None
    os_info: str | None
    cpu_speed: str | None
    ram: str | None
    local_hard_drives: str | None
    parent_configuration_id: int | None
    vendor: CompanyReferenceModel | None
    manufacturer: ManufacturerReferenceModel | None
    questions: list[ConfigurationQuestionModel] | None
    active_flag: bool | None
    management_link: str | None
    remote_link: str | None
    sla: SLAReferenceModel | None
    mobile_guid: str | None
    _info: dict[str, str] | None
    display_vendor_flag: bool | None
    company_location_id: int | None
    show_remote_flag: bool | None
    show_automate_flag: bool | None
    needs_renewal_flag: bool | None
    manufacturer_part_number: str | None
    custom_fields: list[CustomFieldValueModel] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True