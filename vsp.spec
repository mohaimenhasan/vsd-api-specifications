{
    "apis": {
        "children": {
            "/vsps/{id}/eventlogs": {
                "RESTName": "eventlog", 
                "entityName": "EventLog", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "eventlogs"
            }, 
            "/vsps/{id}/hscs": {
                "RESTName": "hsc", 
                "entityName": "HSC", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "hscs"
            }, 
            "/vsps/{id}/vscs": {
                "RESTName": "vsc", 
                "entityName": "VSC", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vscs"
            }, 
            "/vsps/{id}/vsds": {
                "RESTName": "vsd", 
                "entityName": "VSD", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vsds"
            }
        }, 
        "parents": {
            "/vsps": {
                "RESTName": "vsp", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vsps"
            }
        }, 
        "self": {
            "/vsps/{id}": {
                "RESTName": "vsp", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "PUT"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vsps"
            }
        }
    }, 
    "model": {
        "RESTName": "vsp", 
        "attributes": {
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Description of the VSP", 
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
            }, 
            "location": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Installed location of the VSP product", 
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
            }, 
            "name": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name of the VSP", 
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
            }, 
            "productVersion": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Product version number for VSP", 
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
        "description": "System Monitoring details for VSP", 
        "entityName": "VSP", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "/sysmon", 
        "resourceName": "vsps"
    }
}