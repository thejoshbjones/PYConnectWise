from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketSyncsIdEndpoint import ServiceTicketSyncsIdEndpoint
from pywise.endpoints.ServiceTicketSyncsCountEndpoint import ServiceTicketSyncsCountEndpoint
from pywise.models.TicketSyncModel import TicketSyncModel

class ServiceTicketSyncsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ticketSyncs", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketSyncsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTicketSyncsIdEndpoint:
        child = ServiceTicketSyncsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TicketSyncModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TicketSyncModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TicketSyncModel]:
        return self._parse_many(TicketSyncModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TicketSyncModel:
        return self._parse_one(TicketSyncModel, super().make_request("POST", params=params))
        