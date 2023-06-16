from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsTypesCountInfoEndpoint import CompanyContactsTypesCountInfoEndpoint
from pywise.models.CountModel import CountModel

class CompanyContactsTypesCountEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "count", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            CompanyContactsTypesCountInfoEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CountModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CountModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> CountModel:
        return self._parse_one(CountModel, super().make_request("GET", params=params))
        