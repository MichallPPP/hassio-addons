# import miniupnpc
from datetime import datetime
from requests import get
import time
import sys


def update_dns(ip, zone, resource_record_set, ttl, project_name):
    from gcloud import dns
    client = dns.Client(project=project_name)
    zone = client.zone(zone)
    records, page_token = zone.list_resource_record_sets()  # API request
    dns_ip = None
    record_to_remove = None
    for record in records:
        if record.record_type == 'A':
            dns_ip = record.rrdatas[0]
            print(datetime.now(), 'DNS IP: ' + dns_ip, file=sys.stderr)
            record_to_remove = record
            break
    if dns_ip != ip:
        change = zone.changes()
        if record_to_remove is not None:
            change.delete_record_set(record_to_remove)
        ip_record = ip.split()
        new_record = zone.resource_record_set(resource_record_set, 'A', ttl, ip_record)
        change.add_record_set(new_record)
        change.create()  # API request
        while change.status != 'done':
            print(datetime.now(), 'Waiting for changes to complete', file=sys.stderr)
            time.sleep(5)
            change.reload()  # API request
        return ip
    else:
        print(datetime.now(), 'My public IP matches the DNS. No Change required. ' + ip, file=sys.stderr)
        return dns_ip


# Get ip from Router usning UPnP
# u = miniupnpc.UPnP()
# u.discoverdelay = 200
# u.discover()
# u.selectigd()
# public_ip = u.externalipaddress()

oldip = str(sys.argv[1])
zone = str(sys.argv[2])
resource_record_set = str(sys.argv[3])
ttl = sys.argv[4]
project_name = str(sys.argv[5])

hosts=['https://api.ipify.org','https://api.my-ip.io/ip']

for host in hosts:
    try:
        public_ip = get(host).text
        if len(public_ip) > 7 and len(public_ip) <= 15 and public_ip.count('.') == 3:
            break
        else:
            public_ip = ""
            print(datetime.now(), 'Public IP from ' + host + ' doens\'t meet required criteria', file=sys.stderr)
    except:
        public_ip = ""
        print(datetime.now(), 'unable to get ip address from ' + host, file=sys.stderr)

if public_ip == "":
    print(datetime.now(), 'unable to get ip address. Will try again in ' + ttl + ' seconds', file=sys.stderr)
    print(oldip)
    exit()

if oldip != public_ip:
    print(datetime.now(), 'Public IP changed from ' + oldip + ' to ' + public_ip + '. Going to update DNS', file=sys.stderr)
    try:
        oldip = update_dns(public_ip, zone, resource_record_set, ttl, project_name)
        print(datetime.now(), 'Update DNS function ran successfully', file=sys.stderr) 
    except:
        print(datetime.now(), 'Update DNS function failed', file=sys.stderr)
        exit()

print(oldip)