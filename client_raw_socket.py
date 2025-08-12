#!/usr/bin/env python
import socket
import socket, sys, time
from struct import *

HOST = "127.0.0.1"
PORT = "8000"
BASIC_URL = "http://127.0.0.1:8000/"


def main():
    #create a raw socket
    try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except (socket.error , msg):
	    print ('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	    sys.exit()
    packet = ''
    source_ip = '127.0.0.1'
    dest_ip = '127.0.0.1'
    ip_ihl = 5
    ip_ver = 4
    ip_tos = 0
    ip_tot_len = 0	# kernel will fill the correct total length
    ip_id = 54321	#Id of this packet
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = socket.IPPROTO_TCP
    ip_check = 0	# kernel will fill the correct checksum
    ip_saddr = socket.inet_aton ( source_ip )	#Spoof the source ip address if you want to
    ip_daddr = socket.inet_aton ( dest_ip )

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    # the ! in the pack format string means network order
    ip_header = pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

if __name__ == "__main__":
    main()







