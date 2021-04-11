# Home Assistant Add-on: NGINX

## About
Vanilla Nginx containerised for Home Assistant. Simply point nginx to your own configuration file.
## Installation

1. [Add my Hass.io add-ons repository][repository] to your Hass.io instance.
1. Install this add-on.
1. Click the `Save` button to store your configuration.
1. Start the add-on.
1. Check the logs of the add-on to see if everything went well.
1. Carefully configure the add-on to your preferences, see the official documentation for for that.

## How to use
Create your own .conf file or customize the default one that's created after first run

## Configuration

Add-on configuration:

```yaml
conf: "config/nginx.conf"
```

### Option: `conf` (required)

Path to nginx.conf file. If not provided, addon will create one in config/nginx.conf.

[repository]: https://github.com/MichallPPP/hassio-addons