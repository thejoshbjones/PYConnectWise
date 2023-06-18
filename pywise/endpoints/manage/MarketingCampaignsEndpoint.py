from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.MarketingCampaignsIdEndpoint import MarketingCampaignsIdEndpoint
from pywise.endpoints.manage.MarketingCampaignsCountEndpoint import MarketingCampaignsCountEndpoint
from pywise.endpoints.manage.MarketingCampaignsStatusesEndpoint import MarketingCampaignsStatusesEndpoint
from pywise.endpoints.manage.MarketingCampaignsSubTypesEndpoint import MarketingCampaignsSubTypesEndpoint
from pywise.endpoints.manage.MarketingCampaignsTypesEndpoint import MarketingCampaignsTypesEndpoint
from pywise.models.manage.CampaignModel import CampaignModel

class MarketingCampaignsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "campaigns", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            MarketingCampaignsStatusesEndpoint(client, parent_endpoint=self)
        )
        self.subTypes = self.register_child_endpoint(
            MarketingCampaignsSubTypesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            MarketingCampaignsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsIdEndpoint:
        child = MarketingCampaignsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CampaignModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CampaignModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignModel]: The parsed response data.
        """
        return self._parse_many(CampaignModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignModel: The parsed response data.
        """
        return self._parse_one(CampaignModel, super().make_request("POST", params=params).json())
        