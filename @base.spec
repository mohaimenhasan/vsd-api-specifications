{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": [
                "ENTERPRISE",
                "GLOBAL"
            ],
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Specify if scope of entity is Data center or Enterprise level",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "entityScope",
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
            "description": "External object ID. Used for integration with third party systems",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "externalID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": true,
            "uniqueScope": "no"
        }
    ],
    "children": [],
    "model": {
        "create": false,
        "delete": false,
        "description": null,
        "entity_name": null,
        "extends": [],
        "get": false,
        "package": null,
        "resource_name": null,
        "rest_name": null,
        "root": false,
        "update": false
    }
}