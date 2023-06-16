from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdMergeEndpoint import CompanyCompaniesIdMergeEndpoint
from pywise.endpoints.CompanyCompaniesIdUsagesEndpoint import CompanyCompaniesIdUsagesEndpoint
from pywise.endpoints.CompanyCompaniesIdCustomStatusNotesEndpoint import CompanyCompaniesIdCustomStatusNotesEndpoint
from pywise.endpoints.CompanyCompaniesIdGroupsEndpoint import CompanyCompaniesIdGroupsEndpoint
from pywise.endpoints.CompanyCompaniesIdManagementReportNotificationsEndpoint import CompanyCompaniesIdManagementReportNotificationsEndpoint
from pywise.endpoints.CompanyCompaniesIdManagementReportSetupEndpoint import CompanyCompaniesIdManagementReportSetupEndpoint
from pywise.endpoints.CompanyCompaniesIdManagementSummaryReportsEndpoint import CompanyCompaniesIdManagementSummaryReportsEndpoint
from pywise.endpoints.CompanyCompaniesIdNotesEndpoint import CompanyCompaniesIdNotesEndpoint
from pywise.endpoints.CompanyCompaniesIdSitesEndpoint import CompanyCompaniesIdSitesEndpoint
from pywise.endpoints.CompanyCompaniesIdTeamsEndpoint import CompanyCompaniesIdTeamsEndpoint
from pywise.endpoints.CompanyCompaniesIdTracksEndpoint import CompanyCompaniesIdTracksEndpoint
from pywise.endpoints.CompanyCompaniesIdTypeAssociationsEndpoint import CompanyCompaniesIdTypeAssociationsEndpoint
from pywise.models.CompanyModel import CompanyModel

class CompanyCompaniesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.merge = self.register_child_endpoint(
            CompanyCompaniesIdMergeEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyCompaniesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.customStatusNotes = self.register_child_endpoint(
            CompanyCompaniesIdCustomStatusNotesEndpoint(client, parent_endpoint=self)
        )
        self.groups = self.register_child_endpoint(
            CompanyCompaniesIdGroupsEndpoint(client, parent_endpoint=self)
        )
        self.managementReportNotifications = self.register_child_endpoint(
            CompanyCompaniesIdManagementReportNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.managementReportSetup = self.register_child_endpoint(
            CompanyCompaniesIdManagementReportSetupEndpoint(client, parent_endpoint=self)
        )
        self.managementSummaryReports = self.register_child_endpoint(
            CompanyCompaniesIdManagementSummaryReportsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            CompanyCompaniesIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.sites = self.register_child_endpoint(
            CompanyCompaniesIdSitesEndpoint(client, parent_endpoint=self)
        )
        self.teams = self.register_child_endpoint(
            CompanyCompaniesIdTeamsEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self.register_child_endpoint(
            CompanyCompaniesIdTracksEndpoint(client, parent_endpoint=self)
        )
        self.typeAssociations = self.register_child_endpoint(
            CompanyCompaniesIdTypeAssociationsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> CompanyModel:
        return self._parse_one(CompanyModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> CompanyModel:
        return self._parse_one(CompanyModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> CompanyModel:
        return self._parse_one(CompanyModel, super().make_request("PATCH", params=params))
        