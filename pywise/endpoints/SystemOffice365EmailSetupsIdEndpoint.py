from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemOffice365EmailSetupsIdAuthorizeEndpoint import SystemOffice365EmailSetupsIdAuthorizeEndpoint
from pywise.endpoints.SystemOffice365EmailSetupsIdTestConnectionEndpoint import SystemOffice365EmailSetupsIdTestConnectionEndpoint
from pywise.models.Office365EmailSetupModel import Office365EmailSetupModel

class SystemOffice365EmailSetupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.authorize = self.register_child_endpoint(
            SystemOffice365EmailSetupsIdAuthorizeEndpoint(client, parent_endpoint=self)
        )
        self.testConnection = self.register_child_endpoint(
            SystemOffice365EmailSetupsIdTestConnectionEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> Office365EmailSetupModel:
        return self._parse_one(Office365EmailSetupModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> Office365EmailSetupModel:
        return self._parse_one(Office365EmailSetupModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> Office365EmailSetupModel:
        return self._parse_one(Office365EmailSetupModel, super().make_request("PATCH", params=params))
        