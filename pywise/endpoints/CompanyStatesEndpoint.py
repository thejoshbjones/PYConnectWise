from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyStatesIdEndpoint import CompanyStatesIdEndpoint
from pywise.endpoints.CompanyStatesCountEndpoint import CompanyStatesCountEndpoint
from pywise.endpoints.CompanyStatesInfoEndpoint import CompanyStatesInfoEndpoint
from pywise.models.StateModel import StateModel

class CompanyStatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "states", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyStatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyStatesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyStatesIdEndpoint:
        child = CompanyStatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[StateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            StateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[StateModel]:
        return self._parse_many(StateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> StateModel:
        return self._parse_one(StateModel, super().make_request("POST", params=params))
        