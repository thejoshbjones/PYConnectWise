from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementRmaStatusesIdEndpoint import ProcurementRmaStatusesIdEndpoint
from pywise.endpoints.ProcurementRmaStatusesCountEndpoint import ProcurementRmaStatusesCountEndpoint
from pywise.endpoints.ProcurementRmaStatusesInfoEndpoint import ProcurementRmaStatusesInfoEndpoint
from pywise.models.RmaStatusModel import RmaStatusModel

class ProcurementRmaStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaStatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRmaStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRmaStatusesIdEndpoint:
        child = ProcurementRmaStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaStatusModel]:
        return self._parse_many(RmaStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> RmaStatusModel:
        return self._parse_one(RmaStatusModel, super().make_request("POST", params=params))
        