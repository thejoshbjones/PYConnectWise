from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementRmaTagsIdEndpoint import ProcurementRmaTagsIdEndpoint
from pywise.endpoints.ProcurementRmaTagsCountEndpoint import ProcurementRmaTagsCountEndpoint
from pywise.endpoints.ProcurementRmaTagsDefaultEndpoint import ProcurementRmaTagsDefaultEndpoint
from pywise.models.RmaTagModel import RmaTagModel

class ProcurementRmaTagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaTags", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaTagsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            ProcurementRmaTagsDefaultEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRmaTagsIdEndpoint:
        child = ProcurementRmaTagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaTagModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaTagModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaTagModel]:
        return self._parse_many(RmaTagModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> RmaTagModel:
        return self._parse_one(RmaTagModel, super().make_request("POST", params=params))
        