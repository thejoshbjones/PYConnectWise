from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementRmaActionsIdEndpoint import ProcurementRmaActionsIdEndpoint
from pywise.endpoints.ProcurementRmaActionsCountEndpoint import ProcurementRmaActionsCountEndpoint
from pywise.endpoints.ProcurementRmaActionsInfoEndpoint import ProcurementRmaActionsInfoEndpoint
from pywise.models.RmaActionModel import RmaActionModel

class ProcurementRmaActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaActions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaActionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRmaActionsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRmaActionsIdEndpoint:
        child = ProcurementRmaActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaActionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaActionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaActionModel]:
        return self._parse_many(RmaActionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> RmaActionModel:
        return self._parse_one(RmaActionModel, super().make_request("POST", params=params))
        