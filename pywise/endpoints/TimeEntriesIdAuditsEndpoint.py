from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeEntriesIdAuditsIdEndpoint import TimeEntriesIdAuditsIdEndpoint
from pywise.endpoints.TimeEntriesIdAuditsCountEndpoint import TimeEntriesIdAuditsCountEndpoint
from pywise.models.TimeEntryAuditModel import TimeEntryAuditModel

class TimeEntriesIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeEntriesIdAuditsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeEntriesIdAuditsIdEndpoint:
        child = TimeEntriesIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeEntryAuditModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeEntryAuditModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeEntryAuditModel]:
        return self._parse_many(TimeEntryAuditModel, super().make_request("GET", params=params))
        