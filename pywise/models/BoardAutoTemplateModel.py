from __future__ import annotations
from typing import Any
from pywise.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pywise.models.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pywise.models.ServiceItemReferenceModel import ServiceItemReferenceModel
from pywise.models.ServiceTemplateReferenceModel import ServiceTemplateReferenceModel
from pywise.models.BoardReferenceModel import BoardReferenceModel
from enum import Enum
class SummarySetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class DiscussionSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class InternalAnalysisSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class ResolutionSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class TasksSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class DocumentsSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class ResourcesSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class BudgetHoursSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class FinanceInformationSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class SendNotesAsEmailSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'

class BoardAutoTemplateModel(ConnectWiseModel):
    id: int | None
    type: ServiceTypeReferenceModel | None
    subtype: ServiceSubTypeReferenceModel | None
    item: ServiceItemReferenceModel | None
    service_template: ServiceTemplateReferenceModel | None
    board: BoardReferenceModel | None
    summary_setting: SummarySetting | None
    discussion_setting: DiscussionSetting | None
    internal_analysis_setting: InternalAnalysisSetting | None
    resolution_setting: ResolutionSetting | None
    tasks_setting: TasksSetting | None
    documents_setting: DocumentsSetting | None
    resources_setting: ResourcesSetting | None
    budget_hours_setting: BudgetHoursSetting | None
    finance_information_setting: FinanceInformationSetting | None
    send_notes_as_email_setting: SendNotesAsEmailSetting | None
    auto_apply_flag: bool | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True