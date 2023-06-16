from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementOnhandserialnumbersIdEndpoint import ProcurementOnhandserialnumbersIdEndpoint
from pywise.endpoints.ProcurementOnhandserialnumbersCountEndpoint import ProcurementOnhandserialnumbersCountEndpoint
from pywise.models.OnHandSerialNumberModel import OnHandSerialNumberModel

class ProcurementOnhandserialnumbersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "onhandserialnumbers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementOnhandserialnumbersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementOnhandserialnumbersIdEndpoint:
        child = ProcurementOnhandserialnumbersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OnHandSerialNumberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OnHandSerialNumberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OnHandSerialNumberModel]:
        return self._parse_many(OnHandSerialNumberModel, super().make_request("GET", params=params))
        