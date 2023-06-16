from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel
from pywise.models.ManagementSolutionReferenceModel import ManagementSolutionReferenceModel
from enum import Enum
from pywise.models.AgreementReferenceModel import AgreementReferenceModel
from pywise.models.CompanyReferenceModel import CompanyReferenceModel
class DeviceType(str, Enum):
    WorkstationsAndServers = 'WorkstationsAndServers'
    BackupStats = 'BackupStats'
    Servers = 'Servers'
    Workstations = 'Workstations'

class CompanyManagementSummaryModel(ConnectWiseModel):
    id: int | None
    management_solution: ManagementSolutionReferenceModel | None
    group_identifier: str | None
    device_type: DeviceType | None
    agreement: AgreementReferenceModel | None
    snmp_machines: int | None
    total_workstations: int | None
    total_servers: int | None
    total_windows_servers: int | None
    total_windows_workstations: int | None
    total_managed_machines: int | None
    servers_offline: int | None
    servers_disk_space_low: int | None
    failed_backup_jobs: int | None
    total_notifications: int | None
    successful_backup_jobs: int | None
    server_availability: int | None
    viruses_removed: int | None
    spyware_items_removed: int | None
    windows_patches_installed: int | None
    disk_cleanups: int | None
    disk_defragmentations: int | None
    fully_patched_machines: int | None
    missing_one_two_patches_machines: int | None
    missing_three_five_patches_machines: int | None
    missing_more_five_patches_machines: int | None
    missing_unscanned_patches_machines: int | None
    alerts_generated: str | None
    internet_connectivity: float | None
    disk_space_cleaned_mb: int | None
    missing_security_patches: str | None
    cpu_utilization: float | None
    memory_utilization: float | None
    company: CompanyReferenceModel | None
    _info: dict[str, str] | None

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True