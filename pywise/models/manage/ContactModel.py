from __future__ import annotations
from typing import Any
from datetime import datetime
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pywise.models.manage.SiteReferenceModel import SiteReferenceModel
from pywise.models.manage.CountryReferenceModel import CountryReferenceModel
from pywise.models.manage.RelationshipReferenceModel import RelationshipReferenceModel
from pywise.models.manage.ContactDepartmentReferenceModel import ContactDepartmentReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from pywise.models.manage.ContactReferenceModel import ContactReferenceModel
from enum import Enum
from pywise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pywise.models.manage.ContactCommunicationItemModel import ContactCommunicationItemModel
from pywise.models.manage.ContactTypeReferenceModel import ContactTypeReferenceModel
from pywise.models.manage.CustomFieldValueModel import CustomFieldValueModel
from pywise.models.manage.DocumentReferenceModel import DocumentReferenceModel
class Gender(str, Enum):
    Female = 'Female'
    Male = 'Male'
class Presence(str, Enum):
    NoAgent = 'NoAgent'
    Online = 'Online'
    DoNotDisturb = 'DoNotDisturb'
    Away = 'Away'
    Offline = 'Offline'

class ContactModel(ConnectWiseModel):
    id: int | None
    first_name: str | None
    last_name: str | None
    company: CompanyReferenceModel | None
    site: SiteReferenceModel | None
    address_line1: str | None
    address_line2: str | None
    city: str | None
    state: str | None
    zip: str | None
    country: CountryReferenceModel | None
    relationship: RelationshipReferenceModel | None
    relationship_override: str | None
    department: ContactDepartmentReferenceModel | None
    inactive_flag: bool | None
    default_merge_contact_id: int | None
    security_identifier: str | None
    manager_contact: ContactReferenceModel | None
    assistant_contact: ContactReferenceModel | None
    title: str | None
    school: str | None
    nick_name: str | None
    married_flag: bool | None
    children_flag: bool | None
    children: str | None
    significant_other: str | None
    portal_password: str | None
    portal_security_level: int | None
    disable_portal_login_flag: bool | None
    unsubscribe_flag: bool | None
    gender: Gender | None
    birth_day: str | None
    anniversary: str | None
    presence: Presence | None
    mobile_guid: str | None
    facebook_url: str | None
    twitter_url: str | None
    linked_in_url: str | None
    default_phone_type: str | None
    default_phone_nbr: str | None
    default_phone_extension: str | None
    default_billing_flag: bool | None
    default_flag: bool | None
    user_defined_field1: str | None
    user_defined_field2: str | None
    user_defined_field3: str | None
    user_defined_field4: str | None
    user_defined_field5: str | None
    user_defined_field6: str | None
    user_defined_field7: str | None
    user_defined_field8: str | None
    user_defined_field9: str | None
    user_defined_field10: str | None
    company_location: SystemLocationReferenceModel | None
    communication_items: list[ContactCommunicationItemModel] | None
    types: list[ContactTypeReferenceModel] | None
    integrator_tags: list[str] | None
    custom_fields: list[CustomFieldValueModel] | None
    photo: DocumentReferenceModel | None
    ignore_duplicates: bool | None
    _info: dict[str, str] | None
    type_ids: list[int] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True