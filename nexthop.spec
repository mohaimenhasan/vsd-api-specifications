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
            "description": "This is the /32 or /128 next-hop IP address. Currently we support only IPv4 address family.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "ip",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
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
            "description": "The next-hop's route distinguisher. A unique 8 byte long. If not provided one will be generated.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "routeDistinguisher",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": true,
            "uniqueScope": null
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": false,
        "description": "This represents a /32 IPv4 address as the next-hop. In the future can be a /128 IPv6 address.",
        "entity_name": "NextHopAddress",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": false,
        "package": null,
        "resource_name": "nexthops",
        "rest_name": "nexthop",
        "root": false,
        "update": false
    }
}