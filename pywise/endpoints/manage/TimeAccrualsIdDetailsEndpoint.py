from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.TimeAccrualsIdDetailsIdEndpoint import TimeAccrualsIdDetailsIdEndpoint
from pywise.endpoints.manage.TimeAccrualsIdDetailsCountEndpoint import TimeAccrualsIdDetailsCountEndpoint
from pywise.models.manage.TimeAccrualDetailModel import TimeAccrualDetailModel

class TimeAccrualsIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeAccrualsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeAccrualsIdDetailsIdEndpoint:
        child = TimeAccrualsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeAccrualDetailModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeAccrualDetailModel: The parsed response data.
        """
        return self._parse_one(TimeAccrualDetailModel, super().make_request("POST", params=params).json())
        