from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.endpoints.manage.CompanyAddressFormatsEndpoint import CompanyAddressFormatsEndpoint
from pywise.endpoints.manage.CompanyCommunicationTypesEndpoint import CompanyCommunicationTypesEndpoint
from pywise.endpoints.manage.CompanyCompaniesEndpoint import CompanyCompaniesEndpoint
from pywise.endpoints.manage.CompanyCompanyPickerItemsEndpoint import CompanyCompanyPickerItemsEndpoint
from pywise.endpoints.manage.CompanyCompanyTypeAssociationsEndpoint import CompanyCompanyTypeAssociationsEndpoint
from pywise.endpoints.manage.CompanyConfigurationsEndpoint import CompanyConfigurationsEndpoint
from pywise.endpoints.manage.CompanyContactsEndpoint import CompanyContactsEndpoint
from pywise.endpoints.manage.CompanyContactTypeAssociationsEndpoint import CompanyContactTypeAssociationsEndpoint
from pywise.endpoints.manage.CompanyCountriesEndpoint import CompanyCountriesEndpoint
from pywise.endpoints.manage.CompanyEntityTypesEndpoint import CompanyEntityTypesEndpoint
from pywise.endpoints.manage.CompanyManagedDevicesIntegrationsEndpoint import CompanyManagedDevicesIntegrationsEndpoint
from pywise.endpoints.manage.CompanyManagementEndpoint import CompanyManagementEndpoint
from pywise.endpoints.manage.CompanyManagementBackupsEndpoint import CompanyManagementBackupsEndpoint
from pywise.endpoints.manage.CompanyManagementItSolutionsEndpoint import CompanyManagementItSolutionsEndpoint
from pywise.endpoints.manage.CompanyMarketDescriptionsEndpoint import CompanyMarketDescriptionsEndpoint
from pywise.endpoints.manage.CompanyNoteTypesEndpoint import CompanyNoteTypesEndpoint
from pywise.endpoints.manage.CompanyOwnershipTypesEndpoint import CompanyOwnershipTypesEndpoint
from pywise.endpoints.manage.CompanyPortalConfigurationsEndpoint import CompanyPortalConfigurationsEndpoint
from pywise.endpoints.manage.CompanyPortalSecurityLevelsEndpoint import CompanyPortalSecurityLevelsEndpoint
from pywise.endpoints.manage.CompanyPortalSecuritySettingsEndpoint import CompanyPortalSecuritySettingsEndpoint
from pywise.endpoints.manage.CompanyStatesEndpoint import CompanyStatesEndpoint
from pywise.endpoints.manage.CompanyTeamRolesEndpoint import CompanyTeamRolesEndpoint
from pywise.endpoints.manage.CompanyTracksEndpoint import CompanyTracksEndpoint

class CompanyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "company")
        
        self.addressFormats = self.register_child_endpoint(
            CompanyAddressFormatsEndpoint(client, parent_endpoint=self)
        )
        self.communicationTypes = self.register_child_endpoint(
            CompanyCommunicationTypesEndpoint(client, parent_endpoint=self)
        )
        self.companies = self.register_child_endpoint(
            CompanyCompaniesEndpoint(client, parent_endpoint=self)
        )
        self.companyPickerItems = self.register_child_endpoint(
            CompanyCompanyPickerItemsEndpoint(client, parent_endpoint=self)
        )
        self.companyTypeAssociations = self.register_child_endpoint(
            CompanyCompanyTypeAssociationsEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self.register_child_endpoint(
            CompanyConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.contacts = self.register_child_endpoint(
            CompanyContactsEndpoint(client, parent_endpoint=self)
        )
        self.contactTypeAssociations = self.register_child_endpoint(
            CompanyContactTypeAssociationsEndpoint(client, parent_endpoint=self)
        )
        self.countries = self.register_child_endpoint(
            CompanyCountriesEndpoint(client, parent_endpoint=self)
        )
        self.entityTypes = self.register_child_endpoint(
            CompanyEntityTypesEndpoint(client, parent_endpoint=self)
        )
        self.managedDevicesIntegrations = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsEndpoint(client, parent_endpoint=self)
        )
        self.management = self.register_child_endpoint(
            CompanyManagementEndpoint(client, parent_endpoint=self)
        )
        self.managementBackups = self.register_child_endpoint(
            CompanyManagementBackupsEndpoint(client, parent_endpoint=self)
        )
        self.managementItSolutions = self.register_child_endpoint(
            CompanyManagementItSolutionsEndpoint(client, parent_endpoint=self)
        )
        self.marketDescriptions = self.register_child_endpoint(
            CompanyMarketDescriptionsEndpoint(client, parent_endpoint=self)
        )
        self.noteTypes = self.register_child_endpoint(
            CompanyNoteTypesEndpoint(client, parent_endpoint=self)
        )
        self.ownershipTypes = self.register_child_endpoint(
            CompanyOwnershipTypesEndpoint(client, parent_endpoint=self)
        )
        self.portalConfigurations = self.register_child_endpoint(
            CompanyPortalConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.portalSecurityLevels = self.register_child_endpoint(
            CompanyPortalSecurityLevelsEndpoint(client, parent_endpoint=self)
        )
        self.portalSecuritySettings = self.register_child_endpoint(
            CompanyPortalSecuritySettingsEndpoint(client, parent_endpoint=self)
        )
        self.states = self.register_child_endpoint(
            CompanyStatesEndpoint(client, parent_endpoint=self)
        )
        self.teamRoles = self.register_child_endpoint(
            CompanyTeamRolesEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self.register_child_endpoint(
            CompanyTracksEndpoint(client, parent_endpoint=self)
        )