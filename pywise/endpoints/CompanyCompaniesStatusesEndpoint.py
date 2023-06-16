from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesStatusesIdEndpoint import CompanyCompaniesStatusesIdEndpoint
from pywise.endpoints.CompanyCompaniesStatusesCountEndpoint import CompanyCompaniesStatusesCountEndpoint
from pywise.models.CompanyStatusModel import CompanyStatusModel

class CompanyCompaniesStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesStatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesStatusesIdEndpoint:
        child = CompanyCompaniesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyStatusModel]:
        return self._parse_many(CompanyStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyStatusModel:
        return self._parse_one(CompanyStatusModel, super().make_request("POST", params=params))
        