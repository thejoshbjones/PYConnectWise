from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemUserDefinedFieldsIdEndpoint import SystemUserDefinedFieldsIdEndpoint
from pywise.endpoints.SystemUserDefinedFieldsCountEndpoint import SystemUserDefinedFieldsCountEndpoint
from pywise.endpoints.SystemUserDefinedFieldsInfoEndpoint import SystemUserDefinedFieldsInfoEndpoint
from pywise.models.UserDefinedFieldModel import UserDefinedFieldModel

class SystemUserDefinedFieldsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "userDefinedFields", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemUserDefinedFieldsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemUserDefinedFieldsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemUserDefinedFieldsIdEndpoint:
        child = SystemUserDefinedFieldsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UserDefinedFieldModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UserDefinedFieldModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UserDefinedFieldModel]:
        return self._parse_many(UserDefinedFieldModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> UserDefinedFieldModel:
        return self._parse_one(UserDefinedFieldModel, super().make_request("POST", params=params))
        