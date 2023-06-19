from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMyCompanyCorporateStructureIdEndpoint import SystemMyCompanyCorporateStructureIdEndpoint
from pywise.endpoints.manage.SystemMyCompanyCorporateStructureCountEndpoint import SystemMyCompanyCorporateStructureCountEndpoint
from pywise.endpoints.manage.SystemMyCompanyCorporateStructureInfoEndpoint import SystemMyCompanyCorporateStructureInfoEndpoint
from pywise.models.manage.CorporateStructureModel import CorporateStructureModel

class SystemMyCompanyCorporateStructureEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "corporateStructure", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMyCompanyCorporateStructureIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyCompanyCorporateStructureIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyCompanyCorporateStructureIdEndpoint: The initialized SystemMyCompanyCorporateStructureIdEndpoint object.
        """
        child = SystemMyCompanyCorporateStructureIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CorporateStructureModel]:
        """
        Performs a GET request against the /system/myCompany/corporateStructure endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CorporateStructureModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CorporateStructureModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CorporateStructureModel]:
        """
        Performs a GET request against the /system/myCompany/corporateStructure endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CorporateStructureModel]: The parsed response data.
        """
        return self._parse_many(CorporateStructureModel, super().make_request("GET", params=params).json())
        