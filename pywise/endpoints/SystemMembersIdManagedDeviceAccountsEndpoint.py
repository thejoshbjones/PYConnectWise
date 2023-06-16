from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdManagedDeviceAccountsBulkEndpoint import SystemMembersIdManagedDeviceAccountsBulkEndpoint
from pywise.models.ManagedDeviceAccountModel import ManagedDeviceAccountModel

class SystemMembersIdManagedDeviceAccountsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managedDeviceAccounts", parent_endpoint=parent_endpoint)
        
        self.bulk = self.register_child_endpoint(
            SystemMembersIdManagedDeviceAccountsBulkEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagedDeviceAccountModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagedDeviceAccountModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagedDeviceAccountModel]:
        return self._parse_many(ManagedDeviceAccountModel, super().make_request("GET", params=params))
        