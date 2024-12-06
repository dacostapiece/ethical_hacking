#TryHackMe.com
#might req install lib below
#apt install python3-scapy
#sudo apt install python3-scapy
#python3 arp_scanner.py or sudo python3 arp_scanner.py
from scapy.all import *

interface = "eth0"
ip_range = "10.10.X.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))     
