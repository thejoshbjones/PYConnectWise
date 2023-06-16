from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdScheduleentriesCountEndpoint import ServiceTicketsIdScheduleentriesCountEndpoint
from pywise.models.ScheduleEntryReferenceModel import ScheduleEntryReferenceModel

class ServiceTicketsIdScheduleentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "scheduleentries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdScheduleentriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleEntryReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleEntryReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleEntryReferenceModel]:
        return self._parse_many(ScheduleEntryReferenceModel, super().make_request("GET", params=params))
        