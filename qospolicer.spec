{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "1",
            "deprecated": false,
            "description": "Burst Size: The maximum burst size associated with the QoS Policer in kilo-bits; only whole values are supported.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 2147483647,
            "min_length": null,
            "min_value": 1,
            "name": "burst",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Burst"
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
            "description": "Description of the QoS Policer",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "description",
            "orderable": true,
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
            "description": "Name of the QoS Policer",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
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
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "1",
            "deprecated": false,
            "description": "Rate: Bandwidth that is allowed in Mb/s; only whole values supported.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 2147483647,
            "min_length": null,
            "min_value": 1,
            "name": "rate",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Rate"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "QoS Policer ensures that traffic adheres to the stipulated QoS defined in your network. Contains Rate and Burst configurations and can be associated to VLANs.",
        "entity_name": "QosPolicer",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/qos",
        "resource_name": "qospolicers",
        "rest_name": "qospolicer",
        "root": null,
        "update": true,
        "userlabel": "Qos Policer"
    }
}