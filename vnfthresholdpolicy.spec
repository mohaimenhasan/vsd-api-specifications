{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "80",
            "deprecated": false,
            "description": "Threshold for CPU usage",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 100,
            "min_length": null,
            "min_value": 0,
            "name": "CPUThreshold",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "CPU Threshold"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "NONE",
                "SHUTOFF"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "NONE",
            "deprecated": false,
            "description": "Action to be taken on threshold crossover",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "action",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Action"
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
            "description": "Description of VNF agent policy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
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
            "default_value": "80",
            "deprecated": false,
            "description": "Threshold for memory usage",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 100,
            "min_length": null,
            "min_value": 0,
            "name": "memoryThreshold",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Memory Threshold"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "5",
            "deprecated": false,
            "description": "Minimum number of threshold crossover occurrence during monitoring interval before taking specified action",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 20,
            "min_length": null,
            "min_value": 1,
            "name": "minOccurrence",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Minimum Occurrence"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "10",
            "deprecated": false,
            "description": "Monitoring interval (minutes) for threshold crossover occurrences to be considered",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 20,
            "min_length": null,
            "min_value": 5,
            "name": "monitInterval",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Monitoring Interval"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of VNF agent policy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": false,
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
            "default_value": "80",
            "deprecated": false,
            "description": "Threshold for storage usage",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 100,
            "min_length": null,
            "min_value": 0,
            "name": "storageThreshold",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Storage Threshold"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": null,
        "entity_name": "VNFThresholdPolicy",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "vnfthresholdpolicies",
        "rest_name": "vnfthresholdpolicy",
        "root": null,
        "update": true
    }
}