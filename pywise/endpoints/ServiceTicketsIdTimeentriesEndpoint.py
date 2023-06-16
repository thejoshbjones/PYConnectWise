from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdTimeentriesCountEndpoint import ServiceTicketsIdTimeentriesCountEndpoint
from pywise.models.TimeEntryReferenceModel import TimeEntryReferenceModel

class ServiceTicketsIdTimeentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeentries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdTimeentriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeEntryReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeEntryReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeEntryReferenceModel]:
        return self._parse_many(TimeEntryReferenceModel, super().make_request("GET", params=params))
        