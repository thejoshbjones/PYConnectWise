from jinja2 import Template

endpoint_template = Template(
    """from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
{%- if additional_imports is defined %}
{%- for additional_import in additional_imports %}
{{ additional_import }}
{%- endfor %}
{%- endif %}

class {{ endpoint_class }}(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{{ endpoint_path }}", parent_endpoint=parent_endpoint{% if has_id_index %}, id_index="{{ id_index }}"{% endif %})
        {% if child_endpoints is defined %}
        {%- for child_endpoint in child_endpoints %}
        self.{{ child_endpoint.field_name }} = self.register_child_endpoint(
            {{ child_endpoint.class_name }}(client, parent_endpoint=self)
        )
        {%- endfor %}
        {%- endif %}
    {% if has_id_child %}
    def id(self, id: int) -> {{ id_child_endpoint_class }}:
        child = {{ id_child_endpoint_class }}(self.client, parent_endpoint=self)
        child._id = id
        return child
    {% endif %}

    {%- if pagination_model_class is defined %}
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[{{ pagination_model_class }}]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            {{ pagination_model_class }},
            self,
            page_size,
        )
    {% endif %}

    {%- for operation in operations %}
    def {{ operation.name }}(self, data=None, params=None) -> {{ operation.return_type }}:
        {%- if operation.returns_single %}
        return self._parse_one({{operation.return_class}}, super().make_request("{{ operation.name.upper() }}", params=params))
        {% else %}
        return self._parse_many({{operation.return_class}}, super().make_request("{{ operation.name.upper() }}", params=params))
        {% endif %}
    {%- endfor %}
"""
)

top_level_endpoint_template = Template(
    """from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
{%- if additional_imports is defined %}
{%- for additional_import in additional_imports %}
{{ additional_import }}
{%- endfor %}
{%- endif %}

class {{ endpoint_class }}(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "{{ endpoint_path }}")
        {% if child_endpoints is defined %}
        {%- for child_endpoint in child_endpoints %}
        self.{{ child_endpoint.field_name }} = self.register_child_endpoint(
            {{ child_endpoint.class_name }}(client, parent_endpoint=self)
        )
        {%- endfor %}
        {%- endif %}
"""
)

model_template_old = Template(
    """from pywise.models.base.connectwise_model import ConnectWiseModel
{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

class {{ model_class }}():
    def __init__(self, json_dict):
        {%- for field in fields %}
        self.{{ field.name }} : {{ field.type }} = {{ field.type }}({{ field.init_params }})
        {%- endfor %}
        
        super().__init__(json_dict)

"""
)

model_template = Template(
    """from __future__ import annotations
from typing import Any
from pywise.models.utils.naming import to_camel_case
from pywise.models.base.connectwise_model import ConnectWiseModel

{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

{%- if mod_enums is defined %}
{%- for mod_enum in mod_enums %}
class {{ mod_enum.e_name }}(str, Enum):
    {%- for enum_value in mod_enum.fields %}
    {{ enum_value.v_name }} = '{{ enum_value.v_value }}'
    {%- endfor %}

{%- endfor %}
{%- endif %}

class {{ model_class }}(ConnectWiseModel):
    {%- for field in fields %}
    {{ field.name }}: {{ field.type }}
    {%- endfor %}

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
"""
)

client_template = Template(
    """
import os
import base64
import requests
{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

class ConnectWiseManageAPIClient:
    def __init__(
        self,
        client_id,
        company_name,
        company_url,
        public_key,
        private_key,
        codebase=None,
    ):
        self.client_id = client_id
        self.company_name = company_name
        self.company_url = company_url
        self.public_key = public_key
        self.private_key = private_key
        self.codebase = codebase

        if not codebase:
            self.codebase = self.__try_get_codebase_from_api(
                company_url=company_url,
                company_name=company_name,
                headers=self.get_headers(),
            )

        ## ENDPOINT REGISTRATION BELOW ##
        {%- for endpoint in endpoints %}
        self.{{ endpoint.field_name }} = {{ endpoint.class_name }}(self)
        {%- endfor %}

    def get_url(self):
        return f"https://{self.company_url}/{self.codebase.strip('/')}/apis/3.0"

    def __try_get_codebase_from_api(self, company_url, company_name, headers):
        result = ""
        try:
            url = f"https://{company_url}/login/companyinfo/{company_name}"
            result = (
                requests.request("GET", url, headers=headers).json().get("Codebase")
            )
        except:
            result = None
        return result

    def __get_auth_string(self):
        return "Basic " + base64.b64encode(
            bytes(
                f"{self.company_name}+{self.public_key}:{self.private_key}",
                encoding="utf8",
            )
        ).decode("ascii")

    def get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self.__get_auth_string(),
        }
        return headers

"""
)
