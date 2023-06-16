from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdEndpoint import ServiceTicketsIdEndpoint
from pywise.endpoints.ServiceTicketsCountEndpoint import ServiceTicketsCountEndpoint
from pywise.endpoints.ServiceTicketsInfoEndpoint import ServiceTicketsInfoEndpoint
from pywise.endpoints.ServiceTicketsSearchEndpoint import ServiceTicketsSearchEndpoint
from pywise.models.TicketModel import TicketModel

class ServiceTicketsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tickets", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTicketsInfoEndpoint(client, parent_endpoint=self)
        )
        self.search = self.register_child_endpoint(
            ServiceTicketsSearchEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTicketsIdEndpoint:
        child = ServiceTicketsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TicketModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TicketModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TicketModel]:
        return self._parse_many(TicketModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TicketModel:
        return self._parse_one(TicketModel, super().make_request("POST", params=params))
        