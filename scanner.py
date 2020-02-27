#!/usr/bin/python3

import nmap
scanner = nmap.PortScanner()

print("nmap automation tool")
print()
ip_addr = input("Enter IP to scan: ")

scan_type = input("""\nEnter type of scan to run 

                   1. SYN ACK scan
                   2. UDP scan
                   3. Comprehensive scan \n""")

if scan_type == '1':
    print("nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ",scanner[ip_addr]['tcp'].keys())

elif scan_type == '2':    
    print("nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ",scanner[ip_addr]['udp'].keys())

elif scan_type == '3':
    print("nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024','-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocolS())
    print("Open Ports: ",scanner[ip_addr]['tcp'].keys())

else:
    print("Enter valid option")
    

