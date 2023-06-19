from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdEndpoint import MarketingCampaignsTypesIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesCountEndpoint import MarketingCampaignsTypesCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesInfoEndpoint import MarketingCampaignsTypesInfoEndpoint
from pyconnectwise.models.manage.CampaignTypeModel import CampaignTypeModel

class MarketingCampaignsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            MarketingCampaignsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> MarketingCampaignsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsTypesIdEndpoint: The initialized MarketingCampaignsTypesIdEndpoint object.
        """
        child = MarketingCampaignsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CampaignTypeModel]:
        """
        Performs a GET request against the /marketing/campaigns/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CampaignTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignTypeModel]:
        """
        Performs a GET request against the /marketing/campaigns/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignTypeModel]: The parsed response data.
        """
        return self._parse_many(CampaignTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignTypeModel:
        """
        Performs a POST request against the /marketing/campaigns/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignTypeModel: The parsed response data.
        """
        return self._parse_one(CampaignTypeModel, super().make_request("POST", params=params).json())
        