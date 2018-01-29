
schema = "http://json-schema.org/draft-04/schema#"

name = {
    "type": "string",
    "minLength": 4,
}

photo_url = {
    "type": "string"
}

title = {
    "type": "string",
    "minLength": 4,
}

phone = {
    "type": "string",
    "minLength": 10
}

password = {
    "type": "string",
    "minLength": 4
}

email = {
    "type": "string",
    "pattern": "^[^\s@]+@[^\s@]+\.[^\s@]+$",
}

role_id = {
    "type": "number",
}

lab_id = {
    "type": "number",
}

invitee_id = {
    "type": "number",
}

active = {
    "type": "boolean",
}

pending = {
    "type": "boolean",
}

code = {
    "type": "string",
}

add_remove = {
    "type": "object",
    "properties": {
        "add": {
            "type": "array",
            "items": {
                "type": "integer",
            },
        },
        "remove": {
            "type": "array",
            "items": {
                "type": "integer",
            },
        },
    },
    "required": [
        "add",
        "remove",
    ],
}

signin = {
    "$schema": schema,
    "type": "object",
    "properties": {
        "email": email,
        "password": password,
    },
    "required": [
        "email",
        "password"
    ],
    "additionalProperties": False,
}

signup = {
    "$schema": schema,
    "type": "object",
    "properties": {
        "email": email,
        "password": password,
        "role_id": role_id,
    },
    "additionalProperties": False,
    "required": [
        "email",
    ]
}

reset = {
    "$schema": schema,
    "type": "object",
    "properties": {
        "email": email,
        "reset_code": code,
        "password": password,
    },
    "additionalProperties": False,
}

user = {
    "Admin": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "password": password,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "pending": pending,
            "invitee_id": invitee_id,
            "name": name,
            "phone": phone,
            "companies": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "LabAdmin": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "name": name,
            "companies": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "LabAssociate": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "name": name,
            "companies": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "CompanyAdmin": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "name": name,
            "companies": add_remove,
            "clients": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "CompanyAssociate": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "name": name,
            "companies": add_remove,
            "clients": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "ClientManager": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "name": name,
            "companies": add_remove,
            "clients": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "Technician": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "role_id": role_id,
            "lab_id": lab_id,
            "active": active,
            "name": name,
            "companies": add_remove,
            "clients": add_remove,
            "sites": add_remove,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "Own": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "email": email,
            "password": password,
            "name": name,
            "phone": phone,
            "photo_url": photo_url
        },
        "additionalProperties": False,
    },
    "Anonymous": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "password": password,
        },
        "additionalProperties": False,
        "required": [
            "password",
        ],
    },
}

company = {
    "LabAdmin": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "title": title,
            "lab_id": lab_id,
        },
        "additionalProperties": True,
    },
    "LabAssociate": {
        "$schema": schema,
        "type": "object",
        "properties": {
            "title": title,
            "lab_id": lab_id,
        },
        "additionalProperties": True,
    },
}
