{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Priority of the associated Application Group",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "priority",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null
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
            "rest_name": "applicationgroup",
            "update": true
        }
    ],
    "model": {
        "create": null,
        "delete": true,
        "description": "Association object for maintaining the priority of AppliationGroup(s) associated to a Domain",
        "entity_name": "ApplicationGroupBinding",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "applicationgroupbindings",
        "rest_name": "applicationgroupbinding",
        "root": null,
        "update": true
    }
}