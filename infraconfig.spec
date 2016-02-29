{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": [
                "FAILURE",
                "SUCCESS",
                "UNKNOWN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Status of the configuration application",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "configStatus",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Infrastructure Config",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "config",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": "no"
        }
    ],
    "children": [],
    "model": {
        "create": false,
        "delete": false,
        "description": "Represents Infrastructure Config",
        "entity_name": "InfrastructureConfig",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": false,
        "package": "gateway",
        "resource_name": "infraconfig",
        "rest_name": "infraconfig",
        "root": false,
        "update": false
    }
}