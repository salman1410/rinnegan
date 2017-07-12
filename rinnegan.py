#!/usr/bin/python
############################
#         rinnegan         #
# developed by SALMAN ASAD #
#  github.com/salman1410/  #
############################

from urllib2 import *

print \
"""
          _                                   
    _____(_)___  ____  ___  ____ _____ _____  
   / ___/ / __ \/ __ \/ _ \/ __ `/ __ `/ __ \ 
  / /  / / / / / / / /  __/ /_/ / /_/ / / / / 
 /_/  /_/_/ /_/_/ /_/\___/\__, /\__,_/_/ /_/  
                         /____/               
        https://github.com/salman1410         

[1] Whois Lookup
[2] DNS Lookup
[3] Cloudflare Detector
[4] HTTP Header Grabber
"""

def main():
    option = raw_input('\nchoose from available options~:  ')
    if option == '1':
        target = raw_input('\nenter target url or ip~: ')
        whois = "http://api.hackertarget.com/whois/?q=" + target
        r_whois = urlopen(whois).read()
        print (r_whois)
    if option == '2':
        target = raw_input('\nenter target url or ip~: ')
        dns = "http://api.hackertarget.com/dnslookup/?q=" + target
        r_dns = urlopen(dns).read()
        print (r_dns)
    if option == '3':
        target = raw_input('\nenter target url or ip~: ')
        cloud = "http://api.hackertarget.com/dnslookup/?q=" + target
        r_cloud = urlopen(cloud).read()
        if 'cloudflare' in r_cloud:
            print "[+] CLOUDFLARE DETECTED"
        else:
            print "[-] CLOUDFLARE NOT DETECTED"
    if option == '4':
        target = raw_input('\nenter target url or ip~: ')
        header = "http://api.hackertarget.com/httpheaders/?q=" + target
        r_header = urlopen(header).read()
        print (r_header)

try:
	main()
except (KeyboardInterrupt, SystemExit):
    print "\n\t[X]ERROR: aborted by user"
