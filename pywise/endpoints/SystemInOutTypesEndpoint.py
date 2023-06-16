from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInOutTypesIdEndpoint import SystemInOutTypesIdEndpoint
from pywise.endpoints.SystemInOutTypesCountEndpoint import SystemInOutTypesCountEndpoint
from pywise.endpoints.SystemInOutTypesInfoEndpoint import SystemInOutTypesInfoEndpoint
from pywise.models.InOutTypeModel import InOutTypeModel

class SystemInOutTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inOutTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInOutTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemInOutTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInOutTypesIdEndpoint:
        child = SystemInOutTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InOutTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InOutTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InOutTypeModel]:
        return self._parse_many(InOutTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> InOutTypeModel:
        return self._parse_one(InOutTypeModel, super().make_request("POST", params=params))
        