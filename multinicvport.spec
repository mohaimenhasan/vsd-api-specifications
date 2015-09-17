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
      "entityScope": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Specify if scope of entity is Data center or Enterprise level", 
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
        "type": "EntityScope", 
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
    "package": "/sysmon", 
    "resourceName": "multinicvports"
  }
}