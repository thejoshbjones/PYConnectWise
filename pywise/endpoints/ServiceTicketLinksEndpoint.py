from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketLinksIdEndpoint import ServiceTicketLinksIdEndpoint
from pywise.endpoints.ServiceTicketLinksCountEndpoint import ServiceTicketLinksCountEndpoint
from pywise.endpoints.ServiceTicketLinksInfoEndpoint import ServiceTicketLinksInfoEndpoint
from pywise.models.ServiceTicketLinkModel import ServiceTicketLinkModel

class ServiceTicketLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ticketLinks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketLinksCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTicketLinksInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTicketLinksIdEndpoint:
        child = ServiceTicketLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceTicketLinkModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceTicketLinkModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceTicketLinkModel]:
        return self._parse_many(ServiceTicketLinkModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceTicketLinkModel:
        return self._parse_one(ServiceTicketLinkModel, super().make_request("POST", params=params))
        