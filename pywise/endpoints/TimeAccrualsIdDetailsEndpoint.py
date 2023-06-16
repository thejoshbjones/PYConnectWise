from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeAccrualsIdDetailsIdEndpoint import TimeAccrualsIdDetailsIdEndpoint
from pywise.endpoints.TimeAccrualsIdDetailsCountEndpoint import TimeAccrualsIdDetailsCountEndpoint
from pywise.models.TimeAccrualDetailModel import TimeAccrualDetailModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeAccrualDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeAccrualDetailModel,
            self,
            page_size,
        )
    
    def post(self, data=None, params=None) -> TimeAccrualDetailModel:
        return self._parse_one(TimeAccrualDetailModel, super().make_request("POST", params=params))
        