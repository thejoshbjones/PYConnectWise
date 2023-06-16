from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeSheetsIdAuditsIdEndpoint import TimeSheetsIdAuditsIdEndpoint
from pywise.endpoints.TimeSheetsIdAuditsCountEndpoint import TimeSheetsIdAuditsCountEndpoint
from pywise.models.TimeSheetAuditModel import TimeSheetAuditModel

class TimeSheetsIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeSheetsIdAuditsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeSheetsIdAuditsIdEndpoint:
        child = TimeSheetsIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeSheetAuditModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeSheetAuditModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeSheetAuditModel]:
        return self._parse_many(TimeSheetAuditModel, super().make_request("GET", params=params))
        