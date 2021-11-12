#!/usr/bin/env bashio
set -e

bashio::log.info "Starting Azure DDNS..."

export AZURE_TENANT_ID=$(bashio::config 'AZURE_TENANT_ID')
export AZURE_SUBSCRIPTION_ID=$(bashio::config 'AZURE_SUBSCRIPTION_ID')
export AZURE_USERNAME=$(bashio::config 'AZURE_USERNAME')
export AZURE_PASSWORD=$(bashio::config 'AZURE_PASSWORD')
export resource_group_name=$(bashio::config 'resource_group_name')
export dns_zone_name=$(bashio::config 'dns_zone_name')
export record_set_name=$(bashio::config 'record_set_name')
export record_type='A'
export ttl=$(bashio::config 'ttl')

python3 /azuredns.py