{
    "attributes": {
        "action": {
            "allowed_choices": [
                "DROP",
                "FORWARD",
                "REDIRECT"
            ],
            "description": "The flow action. The action can be either FORWARD or DROP.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedApplicationServiceID": {
            "description": "The associated service id.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectID": {
            "description": "The associated network object id.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectType": {
            "allowed_choices": [
                "ACLENTRY_LOCATION",
                "ADDRESS_RANGE",
                "ADDRESS_RANGE_STATE",
                "ALARM",
                "APPD_APPLICATION",
                "APPD_EXTERNAL_APP_SERVICE",
                "APPD_FLOW",
                "APPD_FLOW_FORWARDING_POLICY",
                "APPD_FLOW_SECURITY_POLICY",
                "APPD_SERVICE",
                "APPD_TIER",
                "APPLICATION",
                "AUTO_DISC_GATEWAY",
                "BACK_HAUL_SERVICE_RESP",
                "BGPPEER",
                "BGP_NEIGHBOR",
                "BGP_NEIGHBOR_MED_RESPONSE",
                "BGP_PROFILE",
                "BGP_PROFILE_MED_RESPONSE",
                "BOOTSTRAP",
                "BOOTSTRAP_ACTIVATION",
                "BRIDGEINTERFACE",
                "CERTIFICATE",
                "CHILD_ENTITY_POLICY_CHANGE",
                "CLOUD_MGMT_SYSTEM",
                "CUSTOMER_VRF_SEQUENCENO",
                "DC_CONFIG",
                "DHCP_ALLOC_MESSAGE",
                "DHCP_CONFIG_RESP",
                "DHCP_OPTION",
                "DISKSTATS",
                "DOMAIN",
                "DOMAIN_CONFIG",
                "DOMAIN_CONFIG_RESP",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "DOMAIN_TEMPLATE",
                "DSCP_FORWARDING_CLASS_MAPPING",
                "DSCP_FORWARDING_CLASS_TABLE",
                "EGRESS_ACL",
                "EGRESS_ACL_ENTRY",
                "EGRESS_ACL_TEMPLATE",
                "EGRESS_ACL_TEMPLATE_ENTRY",
                "EGRESS_QOS_MR",
                "EGRESS_QOS_PRIMITIVE",
                "EGRESS_QOS_QUEUE_MR",
                "ENDPOINT",
                "ENTERPRISE",
                "ENTERPRISE_CONFIG",
                "ENTERPRISE_CONFIG_RESP",
                "ENTERPRISE_NETWORK",
                "ENTERPRISE_PERMISSION",
                "ENTERPRISE_PROFILE",
                "ENTERPRISE_SECURED_DATA",
                "ENTERPRISE_SECURITY",
                "ENTITY_METADATA_BINDING",
                "ESI_SEQUENCENO",
                "EVENT_LOG",
                "EVPN_BGP_COMMUNITY_TAG_ENTRY",
                "EVPN_BGP_COMMUNITY_TAG_SEQ_NO",
                "EXPORTIMPORT",
                "EXTERNAL_SERVICE",
                "FLOATINGIP",
                "FLOATINGIP_ACL",
                "FLOATINGIP_ACL_ENTRY",
                "FLOATING_IP_ACL_TEMPLATE",
                "FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "GATEWAY",
                "GATEWAY_CONFIG",
                "GATEWAY_CONFIG_RESP",
                "GATEWAY_SECURED_DATA",
                "GATEWAY_SECURITY",
                "GATEWAY_SECURITY_PROFILE",
                "GATEWAY_SECURITY_PROFILE_REQUEST",
                "GATEWAY_SECURITY_PROFILE_RESPONSE",
                "GATEWAY_SECURITY_REQUEST",
                "GATEWAY_SECURITY_RESPONSE",
                "GATEWAY_SERVICE_CONFIG",
                "GATEWAY_SERVICE_CONFIG_RESP",
                "GATEWAY_TEMPLATE",
                "GATEWAY_VPORT_CONFIG",
                "GATEWAY_VPORT_CONFIG_RESP",
                "GEO_VM_EVENT",
                "GEO_VM_REQ",
                "GEO_VM_RES",
                "GROUP",
                "GROUPKEY_ENCRYPTION_PROFILE",
                "HEALTH_REQ",
                "HOSTINTERFACE",
                "HSC",
                "IKEV2_ENCRYPTION_PROFILE",
                "IKEV2_GATEWAY",
                "INFRASTRUCTURE_CONFIG",
                "INFRASTRUCTURE_GATEWAY_PROFILE",
                "INFRASTRUCTURE_PORT_PROFILE",
                "INFRASTRUCTURE_VSC_PROFILE",
                "INGRESS_ACL",
                "INGRESS_ACL_ENTRY",
                "INGRESS_ACL_TEMPLATE",
                "INGRESS_ACL_TEMPLATE_ENTRY",
                "INGRESS_ADV_FWD",
                "INGRESS_ADV_FWD_ENTRY",
                "INGRESS_ADV_FWD_TEMPLATE",
                "INGRESS_ADV_FWD_TEMPLATE_ENTRY",
                "INGRESS_EXT_SERVICE",
                "INGRESS_EXT_SERVICE_ENTRY",
                "INGRESS_EXT_SERVICE_TEMPLATE",
                "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY",
                "IP_BINDING",
                "JOB",
                "KEYSERVER_MEMBER",
                "KEYSERVER_MONITOR",
                "KEYSERVER_MONITOR_ENCRYPTED_SEED",
                "KEYSERVER_MONITOR_SEED",
                "KEYSERVER_MONITOR_SEK",
                "KEYSERVER_NOTIFICATION",
                "L2DOMAIN",
                "L2DOMAIN_SHARED",
                "L2DOMAIN_TEMPLATE",
                "LDAP_CONFIG",
                "LIBVIRT_INTERFACE",
                "LICENSE",
                "LOCATION",
                "MC_CHANNEL_MAP",
                "MC_LIST",
                "MC_RANGE",
                "METADATA",
                "METADATA_TAG",
                "MIRROR_DESTINATION",
                "MONITORING_PORT",
                "MULTI_NIC_VPORT",
                "NATMAPENTRY",
                "NETWORK_ELEMENT",
                "NETWORK_LAYOUT",
                "NETWORK_MACRO_GROUP",
                "NETWORK_POLICY_GROUP",
                "NEXT_HOP_RESP",
                "NODE_EXECUTION_ERROR",
                "NSGATEWAY",
                "NSGATEWAY_CONFIG",
                "NSGATEWAY_TEMPLATE",
                "NSG_NOTIFICATION",
                "NSPORT",
                "NSPORT_STATIC_CONFIG",
                "NSPORT_TEMPLATE",
                "NSREDUNDANT_GW_GRP",
                "NS_REDUNDANT_PORT",
                "PATCONFIG_CONFIG_RESP",
                "PATNATPOOL",
                "PERMISSION",
                "PERMITTED_ACTION",
                "POLICING_POLICY",
                "POLICY_DECISION",
                "POLICY_GROUP",
                "POLICY_GROUP_TEMPLATE",
                "PORT",
                "PORT_MR",
                "PORT_TEMPLATE",
                "PUBLIC_NETWORK",
                "QOS_PRIMITIVE",
                "RATE_LIMITER",
                "RD_SEQUENCENO",
                "REDUNDANT_GW_GRP",
                "RESYNC",
                "ROUTING_POLICY",
                "ROUTING_POL_MED_RESPONSE",
                "RTRD_ENTITY",
                "RTRD_SEQUENCENO",
                "SERVICES_GATEWAY_RESPONSE",
                "SERVICE_GATEWAY_RESPONSE",
                "SERVICE_VRF_SEQUENCENO",
                "SHAPING_POLICY",
                "SHARED_RESOURCE",
                "SITE",
                "SITE_REQ",
                "SITE_RES",
                "STATIC_ROUTE",
                "STATIC_ROUTE_RESP",
                "STATISTICS",
                "STATSSERVER",
                "STATS_COLLECTOR",
                "STATS_POLICY",
                "STATS_TCA",
                "SUBNET",
                "SUBNET_ENTRY",
                "SUBNET_MAC_ENTRY",
                "SUBNET_POOL_ENTRY",
                "SUBNET_TEMPLATE",
                "SYSTEM_CONFIG",
                "SYSTEM_CONFIG_REQ",
                "SYSTEM_CONFIG_RESP",
                "SYSTEM_MONITORING",
                "UNSUPPORTED",
                "UPLINK_RD",
                "USER",
                "VIRTUAL_IP",
                "VIRTUAL_MACHINE",
                "VIRTUAL_MACHINE_REPORT",
                "VLAN",
                "VLAN_CONFIG_RESPONSE",
                "VLAN_TEMPLATE",
                "VMWARE_RELOAD_CONFIG",
                "VMWARE_VCENTER",
                "VMWARE_VCENTER_CLUSTER",
                "VMWARE_VCENTER_DATACENTER",
                "VMWARE_VCENTER_EAM_CONFIG",
                "VMWARE_VCENTER_HYPERVISOR",
                "VMWARE_VCENTER_VRS_BASE_CONFIG",
                "VMWARE_VCENTER_VRS_CONFIG",
                "VMWARE_VRS_ADDRESS_RANGE",
                "VM_DESCRIPTION",
                "VM_INTERFACE",
                "VNID_SEQUENCENO",
                "VPN_CONNECT",
                "VPORT",
                "VPORTTAG",
                "VPORTTAGTEMPLATE",
                "VPORT_GATEWAY_RESPONSE",
                "VPORT_MEDIATION_REQUEST",
                "VPORT_MIRROR",
                "VPORT_TAG_BASE",
                "VPRN_LABEL_SEQUENCENO",
                "VRS",
                "VSC",
                "VSD",
                "VSD_COMPONENT",
                "VSG_REDUNDANT_PORT",
                "VSP",
                "WAN_SERVICE",
                "ZONE",
                "ZONE_TEMPLATE"
            ],
            "description": "The associated network object type. Refer to API section for supported types.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "destinationAddressOverwrite": {
            "description": "The destination address overwrite. Needs to be in CIDR format x.x.x.x/n",
            "exposed": true,
            "filterable": true,
            "format": "cidr",
            "max_length": 50,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "flowID": {
            "description": "The associated service id.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "priority": {
            "description": "The priority of the flow security policy that determines the order of entries.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "sourceAddressOverwrite": {
            "description": "The source address overwrite. Needs to be in CIDR format x.x.x.x/n",
            "exposed": true,
            "filterable": true,
            "format": "cidr",
            "max_length": 50,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "The security policy on the flow",
        "entity_name": "FlowSecurityPolicy",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "flowsecuritypolicies",
        "rest_name": "flowsecuritypolicy",
        "update": true
    }
}