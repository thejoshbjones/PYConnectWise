from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdManagementReportSetupIdEndpoint import CompanyCompaniesIdManagementReportSetupIdEndpoint
from pywise.models.ManagementReportSetupModel import ManagementReportSetupModel

class CompanyCompaniesIdManagementReportSetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementReportSetup", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> CompanyCompaniesIdManagementReportSetupIdEndpoint:
        child = CompanyCompaniesIdManagementReportSetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementReportSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementReportSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementReportSetupModel]:
        return self._parse_many(ManagementReportSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagementReportSetupModel:
        return self._parse_one(ManagementReportSetupModel, super().make_request("POST", params=params))
        