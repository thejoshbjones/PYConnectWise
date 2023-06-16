from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementRmaStatusesIdNotificationsIdEndpoint import ProcurementRmaStatusesIdNotificationsIdEndpoint
from pywise.endpoints.ProcurementRmaStatusesIdNotificationsCountEndpoint import ProcurementRmaStatusesIdNotificationsCountEndpoint
from pywise.models.RmaStatusNotificationModel import RmaStatusNotificationModel

class ProcurementRmaStatusesIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaStatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRmaStatusesIdNotificationsIdEndpoint:
        child = ProcurementRmaStatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaStatusNotificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaStatusNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaStatusNotificationModel]:
        return self._parse_many(RmaStatusNotificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> RmaStatusNotificationModel:
        return self._parse_one(RmaStatusNotificationModel, super().make_request("POST", params=params))
        