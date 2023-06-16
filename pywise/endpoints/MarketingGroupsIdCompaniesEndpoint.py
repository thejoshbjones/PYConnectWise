from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingGroupsIdCompaniesIdEndpoint import MarketingGroupsIdCompaniesIdEndpoint
from pywise.endpoints.MarketingGroupsIdCompaniesCountEndpoint import MarketingGroupsIdCompaniesCountEndpoint
from pywise.models.MarketingCompanyModel import MarketingCompanyModel

class MarketingGroupsIdCompaniesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companies", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingGroupsIdCompaniesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingGroupsIdCompaniesIdEndpoint:
        child = MarketingGroupsIdCompaniesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MarketingCompanyModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MarketingCompanyModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MarketingCompanyModel]:
        return self._parse_many(MarketingCompanyModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MarketingCompanyModel:
        return self._parse_one(MarketingCompanyModel, super().make_request("POST", params=params))
        