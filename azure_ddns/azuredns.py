import os
import sys
import time
from datetime import datetime
from requests import get
from azure.identity import DefaultAzureCredential
from azure.mgmt.dns import DnsManagementClient

credential = DefaultAzureCredential()
subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
resource_group_name = os.getenv('resource_group_name')
zone_name = os.getenv('dns_zone_name')
record_set_name = os.getenv('record_set_name')
record_type = os.getenv('record_type')
desired_ttl = os.getenv('ttl')
if desired_ttl is not None:
	desired_ttl = int(desired_ttl)
hosts=['https://api.ipify.org','https://api.my-ip.io/ip']

dns_client = DnsManagementClient(
	credential,
	subscription_id
)

def readDNS():
	global record_set
	global records
	global first_record
	global ipv4_address
	global ttl
	global record_type
	try: 
		print(datetime.now(), 'reading Azure DNS', file=sys.stderr)
		record_set = dns_client.record_sets.get(resource_group_name, zone_name, record_set_name, record_type).as_dict()
		records = record_set.get(record_type.lower() + '_records')
		first_record = records[0]
		ipv4_address = first_record.get('ipv4_address')
		ttl = record_set.get('ttl')
		print(datetime.now(), 'DNS is set to ' + ipv4_address, file=sys.stderr)
		return ipv4_address
	except: 
		print(datetime.now(), 'unable to read Azure DNS', file=sys.stderr)
		return ""

def updateDNS(public_ip, desired_ttl):
	global first_record
	global record_set
	global resource_group_name
	global zone_name
	global record_set_name
	global ipv4_address
	global record_type
	print(datetime.now(), 'Updating DNS', file=sys.stderr)
	try:
		first_record.update({'ipv4_address': public_ip})
		record_set = dns_client.record_sets.create_or_update(
			resource_group_name,
			zone_name,
			record_set_name,
			record_type,
			{
				"ttl": desired_ttl,
				record_type.lower() + "records": records
			}
		)
		if readDNS() == public_ip:
			print(datetime.now(), 'DNS sucessfuly updated to ' + public_ip, file=sys.stderr)
		else:
			print(datetime.now(), 'Unable to verify sucessful DNS update', file=sys.stderr)
	except:
		print(datetime.now(), 'Updating DNS failed', file=sys.stderr)


def getPublicIP():
	for host in hosts:
		try:
			public_ip = get(host).text
			if len(public_ip) > 7 and len(public_ip) <= 15 and public_ip.count('.') == 3:
				return public_ip
			else:
				public_ip = ""
				print(datetime.now(), 'Public IP from ' + host + ' doens\'t meet required criteria', file=sys.stderr)
		except:
			public_ip = ""
			print(datetime.now(), 'unable to get ip address from ' + host, file=sys.stderr)
	if public_ip == "":
		print(datetime.now(), 'unable to get ip address. Will try again in ' + ttl + ' seconds', file=sys.stderr)
		return public_ip


ipv4_address = readDNS()
if desired_ttl is None:
	desired_ttl = ttl

while True:
	if ipv4_address == "":
		ipv4_address = readDNS()

	public_ip = getPublicIP()

	if public_ip != "" and ipv4_address != "":
		if public_ip != ipv4_address:
			print(datetime.now(), 'DNS: ' + ipv4_address + ', New public IP: ' + public_ip, file=sys.stderr)
			updateDNS(public_ip, desired_ttl)
		if desired_ttl != ttl:
			print(datetime.now(), 'TTL: ' + str(ttl) + ', Desired TTL: ' + str(desired_ttl), file=sys.stderr)
			updateDNS(public_ip, desired_ttl)
			
	time.sleep(desired_ttl)

