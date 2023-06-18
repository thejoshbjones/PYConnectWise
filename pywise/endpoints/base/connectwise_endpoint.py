from __future__ import annotations
import requests
from pydantic import BaseModel
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.base.connectwise_model import ConnectWiseModel
from typing import Any, TypeVar, Generic, TYPE_CHECKING
from pywise.utils.experimental.patch_maker import PatchGroup
from typing import TypeVar, Type, List, Union

TChildEndpoint = TypeVar("TChildEndpoint", bound="ConnectWiseEndpoint")
TSelf = TypeVar("TSelf", bound="ConnectWiseEndpoint")
T = TypeVar("T", bound="BaseModel")


class ConnectWiseEndpoint:
    """
    ConnectWiseEndpoint is a base class for all ConnectWise API endpoint classes.
    It provides a generic implementation for interacting with the ConnectWise API,
    handling requests, parsing responses into model instances, and managing pagination.

    ConnectWiseEndpoint makes use of a generic type variable TModel, which represents
    the expected ConnectWiseModel type for the endpoint. This allows for type-safe
    handling of model instances throughout the class.

    Each derived class should specify the ConnectWiseModel type it will be working with
    when inheriting from ConnectWiseEndpoint. For example:
    class CompanyEndpoint(ConnectWiseEndpoint[CompanyModel]).

    ConnectWiseEndpoint provides methods for making API requests and handles pagination
    using the PaginatedResponse class. By default, most CRUD methods raise a
    NotImplementedError, which should be overridden in derived classes to provide
    endpoint-specific implementations.

    ConnectWiseEndpoint also supports handling nested endpoints, which are referred to as
    child endpoints. Child endpoints can be registered and accessed through their parent
    endpoint, allowing for easy navigation through related resources in the API.

    Args:
        client: The ConnectWiseAPIClient instance.
        endpoint_base (str): The base URL for the specific endpoint.
        parent_endpoint (ConnectWiseEndpoint, optional): The parent endpoint, if applicable.

    Attributes:
        client (ConnectWiseAPIClient): The ConnectWiseAPIClient instance.
        endpoint_base (str): The base URL for the specific endpoint.
        _parent_endpoint (ConnectWiseEndpoint): The parent endpoint, if applicable.
        model_parser (ModelParser): An instance of the ModelParser class used for parsing API responses.
        _model (Type[TModel]): The model class for the endpoint.
        _id (int): The ID of the current resource, if applicable.
        _child_endpoints (List[ConnectWiseEndpoint]): A list of registered child endpoints.

    Generic Type:
        TModel: The model class for the endpoint.
    """

    def __init__(self, client, endpoint_base, id_index=None, parent_endpoint=None):
        """
        Initialize a ConnectWiseEndpoint instance with the client and endpoint base.

        Args:
            client: The ConnectWiseAPIClient instance.
            endpoint_base (str): The base URL for the specific endpoint.
        """
        self.client = client
        self.endpoint_base = endpoint_base
        self._parent_endpoint = parent_endpoint
        self._id = None
        self._id_index: str | None = id_index
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

    def _url_join(self, *args) -> str:
        """
        Join URL parts into a single URL string.

        Args:
            *args: The URL parts to join.

        Returns:
            str: The joined URL string.
        """
        url_parts = [str(arg).strip("/") for arg in args]
        return "/".join(url_parts)

    def __get_replaced_url(self):
        if self._id is None:
            return self.endpoint_base
        return self.endpoint_base.replace(self._id_index, str(self._id))

    def make_request(
        self, method: str, endpoint=None, data=None, params=None, as_json=True
    ):
        """
        Make an API request using the specified method, endpoint, data, and parameters.
        This function isn't intended for use outside of this class.
        Please use the available CRUD methods as intended.

        Args:
            method (str): The HTTP method to use for the request (e.g., GET, POST, PUT, etc.).
            endpoint (str, optional): The endpoint to make the request to.
            data (dict, optional): The request data to send.
            params (dict, optional): The query parameters to include in the request.
            as_json (bool, optional): Whether to return the JSON response or the Response object. Defaults to True.

        Returns:
            The JSON response or the Response object, depending on the 'as_json' parameter.

        Raises:
            Exception: If the request returns a status code >= 400.
        """
        if not params:
            params = {}
        if not data:
            data = {}

        def build_url(endpoint: ConnectWiseEndpoint) -> str:
            if endpoint._parent_endpoint is not None:
                parent_url = build_url(endpoint._parent_endpoint)
                if endpoint._parent_endpoint._id is not None:
                    return self._url_join(
                        parent_url,
                        endpoint.__get_replaced_url(),
                    )
                else:
                    return self._url_join(parent_url, endpoint.__get_replaced_url())
            else:
                return self._url_join(
                    self.client.get_url(), endpoint.__get_replaced_url()
                )

        url = build_url(self)
        if endpoint:
            url = self._url_join(url, endpoint)

        response = requests.request(
            method, url, headers=self.client.get_headers(), json=data, params=params
        )

        if response.status_code >= 400:
            raise Exception(
                f"Request failed with status code {response.status_code}: {response.text}"
            )

        if as_json:
            return response.json()
        else:
            return response

    def _parse_many(self, model_type: Type[T], data: list[T]) -> list[T]:
        return [model_type.parse_obj(d) for d in data]

    def _parse_one(self, model_type: Type[T], data: dict) -> T:
        return model_type.parse_obj(data)

    def id(self: TSelf, id: int) -> TSelf:
        """
        Set the ID for the current endpoint and its child endpoints.

        Args:
            id (int): The ID to set.
        """
        self._id = id
        return self
