from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdManagementSummaryReportsIdEndpoint import CompanyCompaniesIdManagementSummaryReportsIdEndpoint
from pywise.endpoints.CompanyCompaniesIdManagementSummaryReportsCountEndpoint import CompanyCompaniesIdManagementSummaryReportsCountEndpoint
from pywise.models.CompanyManagementSummaryModel import CompanyManagementSummaryModel

class CompanyCompaniesIdManagementSummaryReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementSummaryReports", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdManagementSummaryReportsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdManagementSummaryReportsIdEndpoint:
        child = CompanyCompaniesIdManagementSummaryReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyManagementSummaryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyManagementSummaryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyManagementSummaryModel]:
        return self._parse_many(CompanyManagementSummaryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyManagementSummaryModel:
        return self._parse_one(CompanyManagementSummaryModel, super().make_request("POST", params=params))
        