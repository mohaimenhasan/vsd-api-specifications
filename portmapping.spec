{
    "attributes": {
        "assocPATIpEntryID": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "privateIP": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "privatePort": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
        },
        "publicIP": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "publicPort": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
        },
        "vport": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "object"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PortMapping",
        "get": true,
        "resource_name": "portmappings",
        "rest_name": "portmapping",
        "update": true
    }
}