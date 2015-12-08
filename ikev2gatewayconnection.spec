{
    "attributes": {
        "associatedIKEv2AuthenticationID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "IKEv2GatewayConnection", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "resource_name": "ikev2gatewayconnections", 
        "rest_name": "ikev2gatewayconnection", 
        "update": true
    }
}