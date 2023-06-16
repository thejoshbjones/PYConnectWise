from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemOffice365EmailSetupsIdEndpoint import SystemOffice365EmailSetupsIdEndpoint
from pywise.endpoints.SystemOffice365EmailSetupsCountEndpoint import SystemOffice365EmailSetupsCountEndpoint
from pywise.models.Office365EmailSetupModel import Office365EmailSetupModel

class SystemOffice365EmailSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemOffice365EmailSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemOffice365EmailSetupsIdEndpoint:
        child = SystemOffice365EmailSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[Office365EmailSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            Office365EmailSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[Office365EmailSetupModel]:
        return self._parse_many(Office365EmailSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> Office365EmailSetupModel:
        return self._parse_one(Office365EmailSetupModel, super().make_request("POST", params=params))
        