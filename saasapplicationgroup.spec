{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Description of the SaaS Breakout Group.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Description"
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
            "description": "Name of the SaaS Breakout Group.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Name"
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "member",
            "rest_name": "saasapplicationtype",
            "update": true
        }
    ],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "Collection of SaaS Application Types.",
        "entity_name": "SaaSApplicationGroup",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": null,
        "resource_name": "saasapplicationgroups",
        "rest_name": "saasapplicationgroup",
        "root": null,
        "template": null,
        "update": true,
        "userlabel": "SaaS Application Group"
    }
}