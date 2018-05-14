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
            "description": "Associated NS Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedNSGatewayID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Network Services Gateway"
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
            "description": "Name of associated NSGateway",
            "exposed": false,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedNSGatewayName",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "NS Gateway Name"
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
            "description": "The segmentation ID (1-4095).",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 4095,
            "min_length": null,
            "min_value": 1,
            "name": "segmentationID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Segmentation ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "VLAN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": "VLAN",
            "deprecated": false,
            "description": "The type of segmentation that is used.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "segmentationType",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Segmentation Type"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "This represents domain segment identifier which is unique for domain per NSGateway.",
        "entity_name": "VNFDomainMapping",
        "extends": [],
        "get": true,
        "package": "vnf",
        "resource_name": "vnfdomainmappings",
        "rest_name": "vnfdomainmapping",
        "root": null,
        "template": false,
        "update": false,
        "userlabel": "VNF Domain Mapping"
    }
}