from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemBundlesCountEndpoint import SystemBundlesCountEndpoint
from pywise.models.manage.BundleResultsCollectionModel import BundleResultsCollectionModel

class SystemBundlesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bundles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemBundlesCountEndpoint(client, parent_endpoint=self)
        )
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BundleResultsCollectionModel:
        """
        Performs a POST request against the /system/bundles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BundleResultsCollectionModel: The parsed response data.
        """
        return self._parse_one(BundleResultsCollectionModel, super().make_request("POST", params=params).json())
        