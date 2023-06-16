from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingGroupsIdContactsIdEndpoint import MarketingGroupsIdContactsIdEndpoint
from pywise.endpoints.MarketingGroupsIdContactsCountEndpoint import MarketingGroupsIdContactsCountEndpoint
from pywise.models.MarketingContactModel import MarketingContactModel

class MarketingGroupsIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingGroupsIdContactsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingGroupsIdContactsIdEndpoint:
        child = MarketingGroupsIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MarketingContactModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MarketingContactModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MarketingContactModel]:
        return self._parse_many(MarketingContactModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MarketingContactModel:
        return self._parse_one(MarketingContactModel, super().make_request("POST", params=params))
        