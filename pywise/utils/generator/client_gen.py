from .templates import client_template
from .fs import save_py_file
import os

def generate_client(client_output_path, endpoints):
    imports = [f"from pywise.endpoints.{endpoint} import {endpoint}" for endpoint in endpoints]
    endpoint_registrations = [{'field_name': endpoint.replace('Endpoint', '').lower(), 'class_name': endpoint} for endpoint in endpoints]
    client_code = client_template.render(imports=imports, endpoints=endpoint_registrations)
    save_py_file(os.path.join(client_output_path, 'client.py'), client_code)