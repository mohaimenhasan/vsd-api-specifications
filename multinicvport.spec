{
    "apis": {
        "children": {
            "/multinicvports/{id}/vports": {
                "RESTName": "vport", 
                "entityName": "VPort", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vports"
            }
        }, 
        "parents": {
            "/vrss/{id}/multinicvports": {
                "RESTName": "vrs", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vrss"
            }
        }, 
        "self": {
            "/multinicvports/{id}": {
                "RESTName": "multinicvport", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "multinicvports"
            }
        }
    }, 
    "model": {
        "RESTName": "multinicvport", 
        "attributes": {
            "name": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name for the Multi NIC VPort.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }
        }, 
        "description": "Encapsulates the Multi NIC VPort information for system monitor entity.", 
        "entityName": "MultiNICVPort", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "/sysmon", 
        "resourceName": "multinicvports"
    }
}