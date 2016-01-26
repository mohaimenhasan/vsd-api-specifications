{
    "attributes": {
        "SEKCreationTime": {
            "description": "SEK Creation Time",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "associatedKeyServerMonitorSEKCreationTime": {
            "description": "The creation time of the associated KeyServer Monitor Seed ID",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "associatedKeyServerMonitorSEKID": {
            "description": "The ID of the associated KeyServer Monitor SEK ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedKeyServerMonitorSeedCreationTime": {
            "description": "The creation time of the associated KeyServer Monitor Seed ID",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "associatedKeyServerMonitorSeedID": {
            "description": "The ID of the associated KeyServer Monitor Seed ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseSecuredDataID": {
            "description": "Enterprise Secured ID record this monitor represents",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "keyServerCertificateSerialNumber": {
            "description": "KeyServer Certificate Serial Number",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents a Keyserver Monitor Encrypted Seed Snapshot",
        "entity_name": "KeyServerMonitorEncryptedSeed",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "keyserver",
        "resource_name": "keyservermonitorencryptedseeds",
        "rest_name": "keyservermonitorencryptedseed",
        "update": true
    }
}