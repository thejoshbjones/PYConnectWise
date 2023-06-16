from __future__ import annotations
import requests
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.base.connectwise_model import ConnectWiseModel
from typing import Any, TypeVar, Generic, TYPE_CHECKING
from pywise.utils.patch_maker import PatchGroup
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint

TChildEndpoint = TypeVar("TChildEndpoint", bound="ConnectWiseEndpoint")
TSelf = TypeVar("TSelf", bound="ConnectWiseTopLevelEndpoint")

class ConnectWiseTopLevelEndpoint:
    def __init__(self, client, endpoint_base):
        """
        Initialize a ConnectWiseEndpoint instance with the client and endpoint base.

        Args:
            client: The ConnectWiseAPIClient instance.
            endpoint_base (str): The base URL for the specific endpoint.
        """
        self.client = client
        self.endpoint_base = endpoint_base
        self._child_endpoints: list[ConnectWiseEndpoint] = []

    def register_child_endpoint(self, child_endpoint: TChildEndpoint) -> TChildEndpoint:
        """
        Register a child endpoint to the current endpoint.

        Args:
            child_endpoint (ConnectWiseEndpoint): The child endpoint instance.

        Returns:
            ConnectWiseEndpoint: The registered child endpoint.
        """
        self._child_endpoints.append(child_endpoint)
        return child_endpoint