from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemNotificationRecipientsIdEndpoint import SystemNotificationRecipientsIdEndpoint
from pywise.endpoints.SystemNotificationRecipientsCountEndpoint import SystemNotificationRecipientsCountEndpoint
from pywise.models.NotificationRecipientModel import NotificationRecipientModel

class SystemNotificationRecipientsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notificationRecipients", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemNotificationRecipientsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemNotificationRecipientsIdEndpoint:
        child = SystemNotificationRecipientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[NotificationRecipientModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            NotificationRecipientModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[NotificationRecipientModel]:
        return self._parse_many(NotificationRecipientModel, super().make_request("GET", params=params))
        