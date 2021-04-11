#!/usr/bin/env bashio
set -e

CONFFILE=$(bashio::config 'conf')

# copy nginx.conf to config folder if doesn't already exist
if [ ! -f $CONFFILE ]; 
    then
        bashio::log.info "$CONFFILE doesn't exist. Copying default file instead."
        CONFFILE=/config/nginx.conf
        cp /etc/nginx.conf /config/
fi 

bashio::log.info "Config set to $CONFFILE"

# start server
bashio::log.info "Running nginx..."
exec nginx -c $CONFFILE < /dev/null
