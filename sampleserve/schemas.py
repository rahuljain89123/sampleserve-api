
schema = "http://json-schema.org/draft-04/schema#"

date = {
    "type": "string",
    "pattern": "\d{2}[-/]\d{2}[-/]\d{4}",
    "pattern": "\d{4}[-/]\d{2}[-/]\d{2}",
}

integer = {
    "type": "integer",
}

number = {
    "type": "number"
}

string = {
    "type": "string"
}

array = {
    "type": "array"
}

boolean = {
    "type": "boolean"
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
