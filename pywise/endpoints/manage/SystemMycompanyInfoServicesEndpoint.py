from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMycompanyInfoServicesIdEndpoint import SystemMycompanyInfoServicesIdEndpoint
from pywise.models.manage.ServiceInfoModel import ServiceInfoModel

class SystemMycompanyInfoServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "services", parent_endpoint=parent_endpoint)
        
    
    
    def id(self, id: int) -> SystemMycompanyInfoServicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyInfoServicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyInfoServicesIdEndpoint: The initialized SystemMycompanyInfoServicesIdEndpoint object.
        """
        child = SystemMycompanyInfoServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceInfoModel]:
        """
        Performs a GET request against the /system/mycompany/info/services endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceInfoModel]:
        """
        Performs a GET request against the /system/mycompany/info/services endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceInfoModel]: The parsed response data.
        """
        return self._parse_many(ServiceInfoModel, super().make_request("GET", params=params).json())
        