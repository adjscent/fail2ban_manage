#!/usr/bin/python3
import re
 
import IP2Location;
 
IP2LocObj = IP2Location.IP2Location();
IP2LocObj.open("IP2LOCATION-LITE-DB1.BIN");
 
f = open('/var/log/fail2ban.log', 'r')
pattern = r".*?Ban\s*?((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))$"
p = re.compile(pattern)
for i in f:
    m = p.match(i)
    if m:
        ip = m.group(1)
        rec = IP2LocObj.get_all(ip);
        print ("%s %s, %s, %s, %s [%s, %s] ZIP: %s TZ: %s" % (ip, rec.country_short, rec.country_long, rec.region, rec.city, rec.latitude, rec.longitude, rec.zipcode, rec.timezone) )
