from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesCommissionsIdEndpoint import SalesCommissionsIdEndpoint
from pywise.endpoints.SalesCommissionsCountEndpoint import SalesCommissionsCountEndpoint
from pywise.models.CommissionModel import CommissionModel

class SalesCommissionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "commissions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesCommissionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesCommissionsIdEndpoint:
        child = SalesCommissionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CommissionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CommissionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CommissionModel]:
        return self._parse_many(CommissionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CommissionModel:
        return self._parse_one(CommissionModel, super().make_request("POST", params=params))
        