# Home Assistant Add-on: Azure DDNS
Dynamic DNS using Microsoft Azure DNS \
Update your A record and TTL in your DNS Zone. 

Addon makes calls to the below servers every TTL (seconds) to find out your Public IP. 
If the IP changes, it makes an API call to Azure to update the A record and TTL.
Note that it will only read your DNS record when the addon is started and then every time your IP changes. \

Primary: https://api.ipify.org \
Secondary: https://api.my-ip.io/ip

## Installation

1. [Add my Hass.io add-ons repository][repository] to your Hass.io instance.
1. Install this add-on.

## Configuration

1. Create a new user Azure AD user.
2. In your DNS Zone go to Access Control > Role Assignements
3. Add Role Assignement
4. Select DNS Role Contributor and press next
5. Add the user account as a member
6. Review & Assign

## Add-on configuration:

```yaml
"AZURE_TENANT_ID": "",
"AZURE_SUBSCRIPTION_ID": "",
"resource_group_name": "example",
"dns_zone_name": "example.net",
"record_set_name": "@",
"ttl": 300,
"AZURE_USERNAME": "",
"AZURE_PASSWORD": ""
```


[repository]: https://github.com/MichallPPP/hassio-addons