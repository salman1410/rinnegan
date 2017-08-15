import os
import io
from urllib import *

print \
"""
          _
    _____(_)___  ____  ___  ____  _____ _____
   / ___/ / __ \/ __ \/ _ \/ __ `/ __ `/ __ |
  / /  / / / / / / / /  __/ /_/ / /_/ / / / /
 /_/  /_/_/ /_/_/ /_/\___/\__, /\__,_/_/ /_/
                         /____/
        https://github.com/salman1410

[1] whois lookup
[2] dns lookup
[3] nmap portscan
[4] robots.txt grabber
"""

def main():
    x = raw_input('enter your choice:~# ')
    url = raw_input('enter target ip or domain:~# ')
    if x=='1':
        cmd="whois " + url
        prcs=os.popen(cmd)
        who=str(prcs.read())
        print(who)
    if x=='2':
        cmd="nslookup " + url
        prcs=os.popen(cmd)
        dns=str(prcs.read())
        print(dns)
    if x=='3':
        cmd="nmap " + url
        prcs=os.popen(cmd)
        nmap=str(prcs.read())
        print(nmap)
    if x=='4':
        link = url+'/'
        req=urlopen(link+"robots.txt", data=None)
        data = io.TextIOWrapper(req, encoding='utf-8')
        print(data.read())

try:
	main()
except (KeyboardInterrupt, SystemExit):
    print "\n\t[X]ERROR: aborted by user"
