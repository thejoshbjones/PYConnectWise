from pywise.utils.generator.templates import (
    endpoint_template,
    model_template,
    top_level_endpoint_template,
)
from pywise.utils.generator.fs import save_py_file
import os
import re
from pywise.utils.naming import to_snake_case


def generate_endpoint_legacy(
    file_output_directory: str,
    path: str,
    path_info: dict,
    relationships: dict,
    id_relationships: dict,
    parent_path: str = "",
):
    cleaned_path = re.sub(r"/{.*?}", "", path).rstrip("/")
    replaced_id_path = (
        path.replace("{parentId}", "{id}")
        .replace("{grandparentId}", "{id}")
        .replace("{reportName}", "{id}")
        .replace("{externalId}", "{id}")
        .rstrip("/")
    )
    subbed_path = replaced_id_path.replace("{id}", "Id")
    endpoint_class = "".join(
        (word[:1].upper() + word[1:]) for word in subbed_path.split("/")
    )
    endpoint_class += "Endpoint"
    model_class = endpoint_class.replace("Endpoint", "Model")
    model_module = model_class.lower()

    operations = list(path_info.keys())

    child_endpoints = relationships.get(cleaned_path, [])
    id_child_endpoints = id_relationships.get(cleaned_path, [])
    print(f"Generating {endpoint_class}")
    for child_endpoint in child_endpoints:
        print(f"    {child_endpoint}")

    additional_imports = []
    for child_endpoint in child_endpoints:
        if "{id}" in child_endpoint:
            continue
        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(
            word.capitalize() for word in child_endpoint.split("/")
        )
        child_endpoint_class += "Endpoint"
        additional_imports.append(
            f"from .{endpoint_class.replace('Endpoint', child_endpoint_class)} import {endpoint_class.replace('Endpoint', child_endpoint_class)}"
        )

    id_child_endpoint_class = None
    has_id_child = False
    if cleaned_path in id_relationships and "{id}" not in path:
        id_child_endpoint_class = endpoint_class.replace("Endpoint", "IdEndpoint")
        additional_imports.append(
            f"from .{id_child_endpoint_class} import {id_child_endpoint_class}"
        )
        has_id_child = True

    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(
            word.capitalize() for word in child_endpoint.split("/")
        )
        child_endpoint_class += "Endpoint"
        child_endpoint_definitions.append(
            {
                "field_name": child_endpoint.split("/")[-1],
                "class_name": endpoint_class.replace("Endpoint", child_endpoint_class),
                "path": child_endpoint_path,
            }
        )

    endpoint_code = endpoint_template.render(
        endpoint_class=endpoint_class,
        model_class=model_class,
        model_module=model_module,
        endpoint_path=path,
        operations=operations,
        child_endpoints=child_endpoint_definitions,
        id_child_endpoints=id_child_endpoints,
        additional_imports=additional_imports,
        id_child_endpoint_class=id_child_endpoint_class,
        has_id_child=has_id_child,
    )

    save_py_file(
        os.path.join(file_output_directory, f"{endpoint_class}.py"), endpoint_code
    )


def generate_model(
    file_output_directory: str, model_name: str, model_schema: dict, models: dict
):
    print(f"            Attempting to generate model: {model_name}")

    cleaned_name = None

    if "." in model_name:
        cleaned_name = model_name.split(".")[-1] + "Model"
    else:
        cleaned_name = model_name + "Model"

    class_name = cleaned_name

    if os.path.exists(os.path.join(file_output_directory, f"{class_name}.py")):
        print(f"            Model already exists: {class_name}")
        return class_name

    properties = model_schema.get("properties")
    fields = []
    imports = []
    enums = []
    has_imported_enum = False

    def convert_type_name(input_type: str) -> str:
        match input_type:
            case "string":
                return "str"
            case "integer":
                return "int"
            case "boolean":
                return "bool"
            case "double":
                return "float"
            case _:
                return "str"

    print(f"            Iterating model properties")
    if properties is not None:
        for field_name, field_schema in properties.items():
            print(f"                Processing property: {field_name}")
            if field_schema.get("$ref") is not None:
                # nested model
                nested_schema = field_schema.get("$ref")
                is_array = False
                if field_schema.get("type") == "array":
                    is_array = True
                nested_model_name = nested_schema.split("/")[-1]
                nested_model_schema = models[nested_model_name]
                nested_class_name = generate_model(
                    file_output_directory,
                    nested_model_name,
                    nested_model_schema,
                    models,
                )
                field_type = nested_class_name
                if is_array:
                    field_type = f"list[{field_type}]"

                ### CONNECTWISE MANAGE API IS DUMB.
                ### It has multilple instances of nullable fields which is great! Because I can type them as <type> | None
                ### But it also has fields that ARE nullable that it doesn't declare as such. Such as addressLine2, mergedParentTicket, etc. inside a TicketModel
                ### Because of this... I basically have to make everything nullable for the time being. Awesome.
                # if is_nullable:
                field_type += " | None"

                fields.append(
                    {
                        "name": to_snake_case(field_name),
                        "type": field_type,
                    }
                )

                if class_name == f"{nested_model_name}Model":
                    print(
                        f"                Skipping import for {nested_model_name}Model as its ourself <{class_name}>"
                    )
                else:
                    imports.append(
                        f"from pywise.models.{nested_model_name}Model import {nested_model_name}Model"
                    )
            else:
                schema_type = field_schema.get("type")
                field_type = None
                if field_schema.get("enum") is not None:
                    enum_values = field_schema.get("enum")
                    enum_name = field_name[:1].upper() + field_name[1:]

                    if not has_imported_enum:
                        imports.append("from enum import Enum")
                        has_imported_enum = True

                    pp_values = []
                    for value in enum_values:
                        if (
                            value.lower() == "none"
                            or value.lower() == "true"
                            or value.lower() == "false"
                        ):
                            pp_values.append(value.upper())
                        else:
                            pp_values.append(value)

                    if enum_name.lower() == "type":
                        enum_name = f"{class_name}Type"

                    enums.append(
                        {
                            "e_name": enum_name,
                            "fields": [
                                {
                                    "v_name": value,
                                    "v_value": value,
                                    "v_type": convert_type_name(schema_type),
                                }
                                for value in pp_values
                            ],
                        }
                    )

                    field_type = enum_name
                else:
                    if schema_type == "array":
                        item_type = field_schema.get("items").get("type")

                        if item_type is None:
                            if field_schema.get("items").get("$ref") is not None:
                                nested_schema = field_schema.get("items").get("$ref")
                                nested_model_name = nested_schema.split("/")[-1]
                                nested_model_schema = models[nested_model_name]
                                nested_class_name = generate_model(
                                    file_output_directory,
                                    nested_model_name,
                                    nested_model_schema,
                                    models,
                                )
                                field_type = f"list[{nested_class_name}]"
                                imports.append(
                                    f"from pywise.models.{nested_class_name} import {nested_class_name}"
                                )
                            else:
                                field_type = "list[Any]"
                        else:
                            field_type = f"list[{convert_type_name(item_type)}]"

                    elif schema_type == "object":
                        props = field_schema.get("additionalProperties")
                        if props is None:
                            item_type = "Any"
                            field_type = f"Any"
                        else:
                            item_type = props.get("type")
                            field_type = f"dict[str, {convert_type_name(item_type)}]"
                    elif schema_type == "number":
                        format = field_schema.get("format")
                        field_type = convert_type_name(format)
                    else:
                        field_type = convert_type_name(schema_type)

                ### CONNECTWISE MANAGE API IS DUMB.
                ### It has multilple instances of nullable fields which is great! Because I can type them as <type> | None
                ### But it also has fields that ARE nullable that it doesn't declare as such. Such as addressLine2, mergedParentTicket, etc. inside a TicketModel
                ### Because of this... I basically have to make everything nullable for the time being. Awesome.
                # if is_nullable:
                field_type += " | None"

                fields.append(
                    {
                        "name": to_snake_case(field_name),
                        "type": field_type,
                    }
                )

    model_code = model_template.render(
        mod_enums=enums, model_class=class_name, imports=imports, fields=fields
    )

    save_py_file(os.path.join(file_output_directory, f"{class_name}.py"), model_code)
    return class_name


def generate_endpoint(
    endpoint_output_directory: str,
    model_output_directory: str,
    path: str,
    path_info: dict,
    relationships: dict,
    models: dict,
):
    # subbed_path = path.replace("{id}", "Id").replace("{parentId}", "ParentId").replace('{grandparentId}', 'GrandparentId').replace('{reportName}', 'ReportName').replace('{externalId}', 'ExternalId').rstrip('/')
    replaced_id_path = (
        path.replace("{parentId}", "{id}")
        .replace("{grandparentId}", "{id}")
        .replace("{reportName}", "{id}")
        .replace("{externalId}", "{id}")
        .rstrip("/")
    )
    subbed_path = replaced_id_path.replace("{id}", "Id")
    endpoint_class = "".join(
        (word[:1].upper() + word[1:]) for word in subbed_path.split("/")
    )
    endpoint_class += "Endpoint"
    model_class = endpoint_class.replace("Endpoint", "Model")
    model_module = model_class.lower()
    is_top_level_endpoint = False

    top_level_check = subbed_path.lstrip("/").split("/")
    if len(top_level_check) == 1:
        is_top_level_endpoint = True

    operations = list(path_info.keys())

    child_endpoints = relationships.get(subbed_path, [])

    print(f"Generating {endpoint_class}")
    for child_endpoint in child_endpoints:
        print(f"    {child_endpoint}")

    id_child_endpoint_class = None
    has_id_child = False
    additional_imports = []
    for child_endpoint in child_endpoints:
        if not child_endpoint:
            continue

        if (
            "Id" in child_endpoint
            or "ParentId" in child_endpoint
            or "GrandparentId" in child_endpoint
            or "ReportName" in child_endpoint
            or "ExternalId" in child_endpoint
        ):
            type_of_id = "Id"
            if "Id" in child_endpoint:
                type_of_id = "Id"

            if "ParentId" in child_endpoint:
                type_of_id = "ParentId"

            if "GrandparentId" in child_endpoint:
                type_of_id = "GrandparentId"

            if "ReportName" in child_endpoint:
                type_of_id = "ReportName"

            if "ExternalId" in child_endpoint:
                type_of_id = "ExternalId"

            id_child_endpoint_class = endpoint_class.replace(
                "Endpoint", f"{type_of_id}Endpoint"
            )
            if endpoint_class == id_child_endpoint_class:
                # what happened here? the parent is it's own child is it's own parent!?
                continue

            additional_imports.append(
                f"from pywise.endpoints.{id_child_endpoint_class} import {id_child_endpoint_class}"
            )
            has_id_child = True
        else:
            child_endpoint_path = child_endpoint
            child_endpoint_class = "".join(
                (word[:1].upper() + word[1:]) for word in child_endpoint.split("/")
            )
            child_endpoint_class += "Endpoint"
            if endpoint_class == child_endpoint_class:
                # what happened here? the parent is it's own child is it's own parent!?
                continue
            additional_imports.append(
                f"from pywise.endpoints.{endpoint_class.replace('Endpoint', child_endpoint_class)} import {endpoint_class.replace('Endpoint', child_endpoint_class)}"
            )

    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        if not child_endpoint:
            continue

        if (
            "Id" in child_endpoint
            or "ParentId" in child_endpoint
            or "GrandparentId" in child_endpoint
            or "ReportName" in child_endpoint
            or "ExternalId" in child_endpoint
        ):
            continue

        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(
            (word[:1].upper() + word[1:]) for word in child_endpoint.split("/")
        )
        child_endpoint_class += "Endpoint"
        field_name = None
        name_segments = child_endpoint.split("/")
        if len(name_segments) == 1:
            field_name = name_segments[0]
        else:
            field_name = name_segments[-1]
        print(f"path is {child_endpoint_path.split('/')[-1]}")
        child_endpoint_definitions.append(
            {
                "field_name": field_name,
                "class_name": endpoint_class.replace("Endpoint", child_endpoint_class),
                "path": child_endpoint_path.split("/")[-1],
            }
        )

    imported_models = []
    op_definitions = []
    pagination_model_class = None
    for operation in operations:
        print(f"        Processing OP: {operation}")
        operation_responses = path_info[operation]["responses"]
        for response in operation_responses.values():
            if response.get("content") is None:
                op_definitions.append(
                    {
                        "name": operation,
                        "return_type": "GenericMessageModel",
                        "return_class": "GenericMessageModel",
                        "returns_single": True,
                    }
                )
            else:
                resp_content = response.get("content")
                schema_object = resp_content.get(list(resp_content)[0]).get("schema")
                schema_ref = None
                is_array = False

                if schema_object.get("type") == "array":
                    is_array = True
                    schema_ref = schema_object.get("items").get("$ref")
                else:
                    schema_ref = schema_object.get("$ref")
                if schema_ref:
                    model_name = schema_ref.split("/")[-1]
                    model_schema = models[model_name]
                    generated_class_name = generate_model(
                        model_output_directory, model_name, model_schema, models
                    )
                    return_type = generated_class_name
                    pagination_model_class = generated_class_name
                    return_class = return_type
                    if is_array:
                        return_type = f"list[{return_type}]"
                    if generated_class_name not in imported_models:
                        print(f"            Importing {generated_class_name}")
                        print(
                            f"                From: pywise.models.{generated_class_name}"
                        )
                        additional_imports.append(
                            f"from pywise.models.{generated_class_name} import {generated_class_name}"
                        )
                        imported_models.append(generated_class_name)
                    op_definitions.append(
                        {
                            "name": operation,
                            "return_type": return_type,
                            "return_class": return_class,
                            "returns_single": not is_array,
                        }
                    )

    id_index = None
    if "{id}" in path:
        id_index = "{id}"
    print(f"           Imports: {additional_imports}")
    endpoint_code = endpoint_template.render(
        endpoint_class=endpoint_class,
        id_index=id_index,
        has_id_index=id_index is not None,
        model_class=model_class,
        model_module=model_module,
        pagination_model_class=pagination_model_class,
        endpoint_path=path.split("/")[-1],
        operations=op_definitions,
        child_endpoints=child_endpoint_definitions,
        additional_imports=additional_imports,
        id_child_endpoint_class=id_child_endpoint_class,
        has_id_child=has_id_child,
    )

    save_py_file(
        os.path.join(endpoint_output_directory, f"{endpoint_class}.py"), endpoint_code
    )
    return is_top_level_endpoint, endpoint_class


def generate_top_level_endpoint(
    endpoint_output_directory: str, path: str, path_info: dict, relationships: dict
):
    # subbed_path = path.replace("{id}", "Id").replace("{parentId}", "ParentId").replace('{grandparentId}', 'GrandparentId').replace('{reportName}', 'ReportName').replace('{externalId}', 'ExternalId').rstrip('/')
    replaced_id_path = (
        path.replace("{parentId}", "{id}")
        .replace("{grandparentId}", "{id}")
        .replace("{reportName}", "{id}")
        .replace("{externalId}", "{id}")
        .rstrip("/")
    )
    subbed_path = replaced_id_path.replace("{id}", "Id")
    endpoint_class = "".join(
        (word[:1].upper() + word[1:]) for word in subbed_path.split("/")
    )
    endpoint_class += "Endpoint"

    child_endpoints = relationships.get(subbed_path, [])

    print(f"Generating {endpoint_class}")
    for child_endpoint in child_endpoints:
        print(f"    {child_endpoint}")

    additional_imports = []
    for child_endpoint in child_endpoints:
        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(
            (word[:1].upper() + word[1:]) for word in child_endpoint.split("/")
        )
        child_endpoint_class += "Endpoint"
        additional_imports.append(
            f"from pywise.endpoints.{endpoint_class.replace('Endpoint', child_endpoint_class)} import {endpoint_class.replace('Endpoint', child_endpoint_class)}"
        )

    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(
            (word[:1].upper() + word[1:]) for word in child_endpoint.split("/")
        )
        child_endpoint_class += "Endpoint"
        child_endpoint_definitions.append(
            {
                "field_name": child_endpoint.split("/")[-1],
                "class_name": endpoint_class.replace("Endpoint", child_endpoint_class),
                "path": child_endpoint_path,
            }
        )

    endpoint_code = top_level_endpoint_template.render(
        endpoint_class=endpoint_class,
        child_endpoints=child_endpoint_definitions,
        additional_imports=additional_imports,
        endpoint_path=path.split("/")[-1],
    )

    save_py_file(
        os.path.join(endpoint_output_directory, f"{endpoint_class}.py"), endpoint_code
    )
    return endpoint_class
