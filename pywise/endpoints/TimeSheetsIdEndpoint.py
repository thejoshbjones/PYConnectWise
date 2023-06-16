from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeSheetsIdApproveEndpoint import TimeSheetsIdApproveEndpoint
from pywise.endpoints.TimeSheetsIdRejectEndpoint import TimeSheetsIdRejectEndpoint
from pywise.endpoints.TimeSheetsIdReverseEndpoint import TimeSheetsIdReverseEndpoint
from pywise.endpoints.TimeSheetsIdSubmitEndpoint import TimeSheetsIdSubmitEndpoint
from pywise.endpoints.TimeSheetsIdAuditsEndpoint import TimeSheetsIdAuditsEndpoint
from pywise.models.TimeSheetModel import TimeSheetModel

class TimeSheetsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.approve = self.register_child_endpoint(
            TimeSheetsIdApproveEndpoint(client, parent_endpoint=self)
        )
        self.reject = self.register_child_endpoint(
            TimeSheetsIdRejectEndpoint(client, parent_endpoint=self)
        )
        self.reverse = self.register_child_endpoint(
            TimeSheetsIdReverseEndpoint(client, parent_endpoint=self)
        )
        self.submit = self.register_child_endpoint(
            TimeSheetsIdSubmitEndpoint(client, parent_endpoint=self)
        )
        self.audits = self.register_child_endpoint(
            TimeSheetsIdAuditsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeSheetModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeSheetModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> TimeSheetModel:
        return self._parse_one(TimeSheetModel, super().make_request("GET", params=params))
        