
from sampleserve.schemas import (
    schema,
    date,
    integer,
    number,
    string,
    array,
    boolean,
    add_remove
)

schedule = {
    "CompanyAdmin": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "site_id": integer,
            "date": date,
            "copy_params": date,
            "tests": add_remove,
            "gauged_wells": add_remove,
        },
        "additionalProperties": True,
    },
    "CompanyAssociate": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "site_id": integer,
            "date": date,
            "copy_params": date,
            "tests": add_remove,
            "gauged_wells": add_remove,
        },
        "additionalProperties": True,
    },
    "ClientManager": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "site_id": integer,
            "date": date,
            "copy_params": date,
            "tests": add_remove,
            "gauged_wells": add_remove,
        },
        "additionalProperties": True,
    },
    "Own": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "site_id": integer,
            "date": date,
            "copy_params": date,
            "tests": add_remove,
            "gauged_wells": add_remove,
        },
        "additionalProperties": True,
    },
}

post_site = {
    "$schema": schema,
    "type": "object",
    "properties": {
        "title": string,
        "client_id": integer,
        "state_id": integer,
        "city": string,
    },
    "required": [
        "title",
        "state_id",
        "city",
    ],
    "additionalProperties": True,
}

patch_site = {
    "$schema": schema,
    "type": "object",
    "properties": {
        "title": string,
        "client_id": integer,
        "state_id": integer,
        "city": string,
    },
    "additionalProperties": True,
}










