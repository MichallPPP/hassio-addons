# Home Assistant Add-on: NGINX
Vanilla Nginx containerised for Home Assistant. Simply point nginx to your own configuration file.

## Installation

1. [Add my Hass.io add-ons repository][repository] to your Hass.io instance.
1. Install this add-on.

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