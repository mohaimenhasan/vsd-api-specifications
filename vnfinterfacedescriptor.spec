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
            "description": "Device name associated with this interface",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 30,
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
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "LAN",
                "MANAGEMENT",
                "WAN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "MANAGEMENT",
            "deprecated": false,
            "description": "Type of VNF interface",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "type",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Interface Type"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "Represent VNF interface descriptor",
        "entity_name": "VNFInterfaceDescriptor",
        "extends": [],
        "get": true,
        "package": "vnf",
        "resource_name": "vnfinterfacedescriptors",
        "rest_name": "vnfinterfacedescriptor",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "VNF Interface Descriptor"
    }
}