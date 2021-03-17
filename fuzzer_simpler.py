#!/bin/python3


#This is a fuzzer containing only the necessary bits.


import socket
import time
import sys

#Usage:
#python3 fuzzer_simpler.py [RHOST] [RPORT] [Max Byte]
#./fuzzer_simpler.py [RHOST] [RPORT] [Max Byte]

rhost = sys.argv[1]
rport = int(sys.argv[2])
max = int(sys.argv[3])

#Initial size
size = 100

while size < max:
	print("Sending " + str(size) + " \"A\" characters...\n")
	inputBuffer = b'A' * size
	#Creating a socket, connecting to the host, and sending 'A's
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.connect((rhost,rport))
		s.send(inputBuffer)
		s.close()
	time.sleep(5)
	size += 100
