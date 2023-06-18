from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceTemplatesIdEndpoint import ServiceTemplatesIdEndpoint
from pywise.endpoints.manage.ServiceTemplatesCountEndpoint import ServiceTemplatesCountEndpoint
from pywise.endpoints.manage.ServiceTemplatesInfoEndpoint import ServiceTemplatesInfoEndpoint
from pywise.models.manage.ServiceTemplateModel import ServiceTemplateModel

class ServiceTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "templates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTemplatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceTemplatesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTemplatesIdEndpoint:
        child = ServiceTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceTemplateModel]:
        """
        Performs a GET request against the /service/templates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceTemplateModel]:
        """
        Performs a GET request against the /service/templates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceTemplateModel]: The parsed response data.
        """
        return self._parse_many(ServiceTemplateModel, super().make_request("GET", params=params).json())
        