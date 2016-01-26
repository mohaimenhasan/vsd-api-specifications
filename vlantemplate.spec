{
    "attributes": {
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "value": {
            "description": "value of VLAN",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer",
            "min_value": 0,
            "max_value": 4096,
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents VLAN Template under a PORT Template object.",
        "entity_name": "VLANTemplate",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "vlantemplates",
        "rest_name": "vlantemplate",
        "update": true
    }
}