from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingGroupsIdEndpoint import MarketingGroupsIdEndpoint
from pywise.endpoints.MarketingGroupsCountEndpoint import MarketingGroupsCountEndpoint
from pywise.models.GroupModel import GroupModel

class MarketingGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingGroupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingGroupsIdEndpoint:
        child = MarketingGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[GroupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            GroupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[GroupModel]:
        return self._parse_many(GroupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> GroupModel:
        return self._parse_one(GroupModel, super().make_request("POST", params=params))
        