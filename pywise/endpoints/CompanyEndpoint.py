from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.CompanyAddressFormatsEndpoint import CompanyAddressFormatsEndpoint
from pywise.endpoints.CompanyCommunicationTypesEndpoint import CompanyCommunicationTypesEndpoint
from pywise.endpoints.CompanyCompaniesEndpoint import CompanyCompaniesEndpoint
from pywise.endpoints.CompanyCompanyPickerItemsEndpoint import CompanyCompanyPickerItemsEndpoint
from pywise.endpoints.CompanyCompanyTypeAssociationsEndpoint import CompanyCompanyTypeAssociationsEndpoint
from pywise.endpoints.CompanyConfigurationsEndpoint import CompanyConfigurationsEndpoint
from pywise.endpoints.CompanyContactsEndpoint import CompanyContactsEndpoint
from pywise.endpoints.CompanyContactTypeAssociationsEndpoint import CompanyContactTypeAssociationsEndpoint
from pywise.endpoints.CompanyCountriesEndpoint import CompanyCountriesEndpoint
from pywise.endpoints.CompanyEntityTypesEndpoint import CompanyEntityTypesEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsEndpoint import CompanyManagedDevicesIntegrationsEndpoint
from pywise.endpoints.CompanyManagementEndpoint import CompanyManagementEndpoint
from pywise.endpoints.CompanyManagementBackupsEndpoint import CompanyManagementBackupsEndpoint
from pywise.endpoints.CompanyManagementItSolutionsEndpoint import CompanyManagementItSolutionsEndpoint
from pywise.endpoints.CompanyMarketDescriptionsEndpoint import CompanyMarketDescriptionsEndpoint
from pywise.endpoints.CompanyNoteTypesEndpoint import CompanyNoteTypesEndpoint
from pywise.endpoints.CompanyOwnershipTypesEndpoint import CompanyOwnershipTypesEndpoint
from pywise.endpoints.CompanyPortalConfigurationsEndpoint import CompanyPortalConfigurationsEndpoint
from pywise.endpoints.CompanyPortalSecurityLevelsEndpoint import CompanyPortalSecurityLevelsEndpoint
from pywise.endpoints.CompanyPortalSecuritySettingsEndpoint import CompanyPortalSecuritySettingsEndpoint
from pywise.endpoints.CompanyStatesEndpoint import CompanyStatesEndpoint
from pywise.endpoints.CompanyTeamRolesEndpoint import CompanyTeamRolesEndpoint
from pywise.endpoints.CompanyTracksEndpoint import CompanyTracksEndpoint

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