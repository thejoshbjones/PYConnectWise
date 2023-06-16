from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemEmailConnectorsIdEndpoint import SystemEmailConnectorsIdEndpoint
from pywise.endpoints.SystemEmailConnectorsCountEndpoint import SystemEmailConnectorsCountEndpoint
from pywise.endpoints.SystemEmailConnectorsInfoEndpoint import SystemEmailConnectorsInfoEndpoint
from pywise.models.EmailConnectorModel import EmailConnectorModel

class SystemEmailConnectorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailConnectors", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailConnectorsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemEmailConnectorsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemEmailConnectorsIdEndpoint:
        child = SystemEmailConnectorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EmailConnectorModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EmailConnectorModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EmailConnectorModel]:
        return self._parse_many(EmailConnectorModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> EmailConnectorModel:
        return self._parse_one(EmailConnectorModel, super().make_request("POST", params=params))
        