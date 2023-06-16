from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.SystemAllowedoriginsEndpoint import SystemAllowedoriginsEndpoint
from pywise.endpoints.SystemApiMembersEndpoint import SystemApiMembersEndpoint
from pywise.endpoints.SystemAudittrailEndpoint import SystemAudittrailEndpoint
from pywise.endpoints.SystemAuthAnvilsEndpoint import SystemAuthAnvilsEndpoint
from pywise.endpoints.SystemAutoSyncTimeEndpoint import SystemAutoSyncTimeEndpoint
from pywise.endpoints.SystemBundlesEndpoint import SystemBundlesEndpoint
from pywise.endpoints.SystemCallbacksEndpoint import SystemCallbacksEndpoint
from pywise.endpoints.SystemCertificationsEndpoint import SystemCertificationsEndpoint
from pywise.endpoints.SystemConnectWiseHostedScreensEndpoint import SystemConnectWiseHostedScreensEndpoint
from pywise.endpoints.SystemConnectwisehostedsetupsEndpoint import SystemConnectwisehostedsetupsEndpoint
from pywise.endpoints.SystemCustomReportsEndpoint import SystemCustomReportsEndpoint
from pywise.endpoints.SystemCwTimeZonesEndpoint import SystemCwTimeZonesEndpoint
from pywise.endpoints.SystemDepartmentsEndpoint import SystemDepartmentsEndpoint
from pywise.endpoints.SystemDocumentsEndpoint import SystemDocumentsEndpoint
from pywise.endpoints.SystemEmailConnectorsEndpoint import SystemEmailConnectorsEndpoint
from pywise.endpoints.SystemEmailExclusionsEndpoint import SystemEmailExclusionsEndpoint
from pywise.endpoints.SystemEmailTokensEndpoint import SystemEmailTokensEndpoint
from pywise.endpoints.SystemEPayConfigurationsEndpoint import SystemEPayConfigurationsEndpoint
from pywise.endpoints.SystemExperimentsEndpoint import SystemExperimentsEndpoint
from pywise.endpoints.SystemImapsEndpoint import SystemImapsEndpoint
from pywise.endpoints.SystemInfoEndpoint import SystemInfoEndpoint
from pywise.endpoints.SystemInOutBoardsEndpoint import SystemInOutBoardsEndpoint
from pywise.endpoints.SystemInOutTypesEndpoint import SystemInOutTypesEndpoint
from pywise.endpoints.SystemIntegratorloginsEndpoint import SystemIntegratorloginsEndpoint
from pywise.endpoints.SystemIntegratorTagsEndpoint import SystemIntegratorTagsEndpoint
from pywise.endpoints.SystemKpiCategoriesEndpoint import SystemKpiCategoriesEndpoint
from pywise.endpoints.SystemKpisEndpoint import SystemKpisEndpoint
from pywise.endpoints.SystemLdapConfigurationsEndpoint import SystemLdapConfigurationsEndpoint
from pywise.endpoints.SystemLinksEndpoint import SystemLinksEndpoint
from pywise.endpoints.SystemLocationsEndpoint import SystemLocationsEndpoint
from pywise.endpoints.SystemManagementNetworkSecuritiesEndpoint import SystemManagementNetworkSecuritiesEndpoint
from pywise.endpoints.SystemMembersEndpoint import SystemMembersEndpoint
from pywise.endpoints.SystemMenuentriesEndpoint import SystemMenuentriesEndpoint
from pywise.endpoints.SystemMyMembersEndpoint import SystemMyMembersEndpoint
from pywise.endpoints.SystemMySecurityEndpoint import SystemMySecurityEndpoint
from pywise.endpoints.SystemNotificationRecipientsEndpoint import SystemNotificationRecipientsEndpoint
from pywise.endpoints.SystemOsgradeweightsEndpoint import SystemOsgradeweightsEndpoint
from pywise.endpoints.SystemParsingTypesEndpoint import SystemParsingTypesEndpoint
from pywise.endpoints.SystemParsingVariablesEndpoint import SystemParsingVariablesEndpoint
from pywise.endpoints.SystemPortalReportsEndpoint import SystemPortalReportsEndpoint
from pywise.endpoints.SystemQuoteLinkSetupEndpoint import SystemQuoteLinkSetupEndpoint
from pywise.endpoints.SystemReportCardsEndpoint import SystemReportCardsEndpoint
from pywise.endpoints.SystemReportsEndpoint import SystemReportsEndpoint
from pywise.endpoints.SystemSecurityrolesEndpoint import SystemSecurityrolesEndpoint
from pywise.endpoints.SystemSettingsEndpoint import SystemSettingsEndpoint
from pywise.endpoints.SystemSetupScreensEndpoint import SystemSetupScreensEndpoint
from pywise.endpoints.SystemSkillCategoriesEndpoint import SystemSkillCategoriesEndpoint
from pywise.endpoints.SystemSkillsEndpoint import SystemSkillsEndpoint
from pywise.endpoints.SystemSsoConfigurationsEndpoint import SystemSsoConfigurationsEndpoint
from pywise.endpoints.SystemSsoUsersEndpoint import SystemSsoUsersEndpoint
from pywise.endpoints.SystemStandardNotesEndpoint import SystemStandardNotesEndpoint
from pywise.endpoints.SystemSurveysEndpoint import SystemSurveysEndpoint
from pywise.endpoints.SystemTimeZoneSetupsEndpoint import SystemTimeZoneSetupsEndpoint
from pywise.endpoints.SystemTodayPageCategoriesEndpoint import SystemTodayPageCategoriesEndpoint
from pywise.endpoints.SystemUserDefinedFieldsEndpoint import SystemUserDefinedFieldsEndpoint
from pywise.endpoints.SystemWorkflowsEndpoint import SystemWorkflowsEndpoint

class SystemEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "system")
        
        self.allowedorigins = self.register_child_endpoint(
            SystemAllowedoriginsEndpoint(client, parent_endpoint=self)
        )
        self.apiMembers = self.register_child_endpoint(
            SystemApiMembersEndpoint(client, parent_endpoint=self)
        )
        self.audittrail = self.register_child_endpoint(
            SystemAudittrailEndpoint(client, parent_endpoint=self)
        )
        self.authAnvils = self.register_child_endpoint(
            SystemAuthAnvilsEndpoint(client, parent_endpoint=self)
        )
        self.autoSyncTime = self.register_child_endpoint(
            SystemAutoSyncTimeEndpoint(client, parent_endpoint=self)
        )
        self.bundles = self.register_child_endpoint(
            SystemBundlesEndpoint(client, parent_endpoint=self)
        )
        self.callbacks = self.register_child_endpoint(
            SystemCallbacksEndpoint(client, parent_endpoint=self)
        )
        self.certifications = self.register_child_endpoint(
            SystemCertificationsEndpoint(client, parent_endpoint=self)
        )
        self.connectWiseHostedScreens = self.register_child_endpoint(
            SystemConnectWiseHostedScreensEndpoint(client, parent_endpoint=self)
        )
        self.connectwisehostedsetups = self.register_child_endpoint(
            SystemConnectwisehostedsetupsEndpoint(client, parent_endpoint=self)
        )
        self.customReports = self.register_child_endpoint(
            SystemCustomReportsEndpoint(client, parent_endpoint=self)
        )
        self.cwTimeZones = self.register_child_endpoint(
            SystemCwTimeZonesEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            SystemDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.documents = self.register_child_endpoint(
            SystemDocumentsEndpoint(client, parent_endpoint=self)
        )
        self.emailConnectors = self.register_child_endpoint(
            SystemEmailConnectorsEndpoint(client, parent_endpoint=self)
        )
        self.emailExclusions = self.register_child_endpoint(
            SystemEmailExclusionsEndpoint(client, parent_endpoint=self)
        )
        self.emailTokens = self.register_child_endpoint(
            SystemEmailTokensEndpoint(client, parent_endpoint=self)
        )
        self.ePayConfigurations = self.register_child_endpoint(
            SystemEPayConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.experiments = self.register_child_endpoint(
            SystemExperimentsEndpoint(client, parent_endpoint=self)
        )
        self.imaps = self.register_child_endpoint(
            SystemImapsEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemInfoEndpoint(client, parent_endpoint=self)
        )
        self.inOutBoards = self.register_child_endpoint(
            SystemInOutBoardsEndpoint(client, parent_endpoint=self)
        )
        self.inOutTypes = self.register_child_endpoint(
            SystemInOutTypesEndpoint(client, parent_endpoint=self)
        )
        self.integratorlogins = self.register_child_endpoint(
            SystemIntegratorloginsEndpoint(client, parent_endpoint=self)
        )
        self.integratorTags = self.register_child_endpoint(
            SystemIntegratorTagsEndpoint(client, parent_endpoint=self)
        )
        self.kpiCategories = self.register_child_endpoint(
            SystemKpiCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.kpis = self.register_child_endpoint(
            SystemKpisEndpoint(client, parent_endpoint=self)
        )
        self.ldapConfigurations = self.register_child_endpoint(
            SystemLdapConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.links = self.register_child_endpoint(
            SystemLinksEndpoint(client, parent_endpoint=self)
        )
        self.locations = self.register_child_endpoint(
            SystemLocationsEndpoint(client, parent_endpoint=self)
        )
        self.managementNetworkSecurities = self.register_child_endpoint(
            SystemManagementNetworkSecuritiesEndpoint(client, parent_endpoint=self)
        )
        self.members = self.register_child_endpoint(
            SystemMembersEndpoint(client, parent_endpoint=self)
        )
        self.menuentries = self.register_child_endpoint(
            SystemMenuentriesEndpoint(client, parent_endpoint=self)
        )
        self.myMembers = self.register_child_endpoint(
            SystemMyMembersEndpoint(client, parent_endpoint=self)
        )
        self.mySecurity = self.register_child_endpoint(
            SystemMySecurityEndpoint(client, parent_endpoint=self)
        )
        self.notificationRecipients = self.register_child_endpoint(
            SystemNotificationRecipientsEndpoint(client, parent_endpoint=self)
        )
        self.osgradeweights = self.register_child_endpoint(
            SystemOsgradeweightsEndpoint(client, parent_endpoint=self)
        )
        self.parsingTypes = self.register_child_endpoint(
            SystemParsingTypesEndpoint(client, parent_endpoint=self)
        )
        self.parsingVariables = self.register_child_endpoint(
            SystemParsingVariablesEndpoint(client, parent_endpoint=self)
        )
        self.portalReports = self.register_child_endpoint(
            SystemPortalReportsEndpoint(client, parent_endpoint=self)
        )
        self.quoteLinkSetup = self.register_child_endpoint(
            SystemQuoteLinkSetupEndpoint(client, parent_endpoint=self)
        )
        self.reportCards = self.register_child_endpoint(
            SystemReportCardsEndpoint(client, parent_endpoint=self)
        )
        self.reports = self.register_child_endpoint(
            SystemReportsEndpoint(client, parent_endpoint=self)
        )
        self.securityroles = self.register_child_endpoint(
            SystemSecurityrolesEndpoint(client, parent_endpoint=self)
        )
        self.settings = self.register_child_endpoint(
            SystemSettingsEndpoint(client, parent_endpoint=self)
        )
        self.setupScreens = self.register_child_endpoint(
            SystemSetupScreensEndpoint(client, parent_endpoint=self)
        )
        self.skillCategories = self.register_child_endpoint(
            SystemSkillCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.skills = self.register_child_endpoint(
            SystemSkillsEndpoint(client, parent_endpoint=self)
        )
        self.ssoConfigurations = self.register_child_endpoint(
            SystemSsoConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.ssoUsers = self.register_child_endpoint(
            SystemSsoUsersEndpoint(client, parent_endpoint=self)
        )
        self.standardNotes = self.register_child_endpoint(
            SystemStandardNotesEndpoint(client, parent_endpoint=self)
        )
        self.surveys = self.register_child_endpoint(
            SystemSurveysEndpoint(client, parent_endpoint=self)
        )
        self.timeZoneSetups = self.register_child_endpoint(
            SystemTimeZoneSetupsEndpoint(client, parent_endpoint=self)
        )
        self.todayPageCategories = self.register_child_endpoint(
            SystemTodayPageCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.userDefinedFields = self.register_child_endpoint(
            SystemUserDefinedFieldsEndpoint(client, parent_endpoint=self)
        )
        self.workflows = self.register_child_endpoint(
            SystemWorkflowsEndpoint(client, parent_endpoint=self)
        )