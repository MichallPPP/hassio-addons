#!/usr/bin/env bashio
set -e

service_account_path=$(bashio::config 'service_account_path')

bashio::log.info "Checking credentials in $service_account_path"
if ! bashio::fs.file_exists "${service_account_path}"; then
        bashio::log.error "$service_account_path doesn't exist."
        bashio::log.info "Save service account json file in $service_account_path and restart the addon."
        exit
fi 

bashio::log.info "Starting DDNS..."

export GOOGLE_APPLICATION_CREDENTIALS=$service_account_path
ZONE=$(bashio::config 'zone')
RESOURCE_RECORD_SET=$(bashio::config 'resource_record_set')
TTL=$(bashio::config 'ttl')
PROJECT_NAME=$(bashio::config 'project_name')

oldip=""
myip="0.0.0.0"
while [ : ]
do 
    myip="$(python3 /googledns.py $myip $ZONE $RESOURCE_RECORD_SET $TTL $PROJECT_NAME)"
    if [[ $oldip != $myip ]]; then
        oldip=$myip
    fi
    sleep "${TTL}"
done