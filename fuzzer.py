#!/bin/python3


#THIS IS A VERY CRUDE FUZZER!
#FOR EVEN SIMPLER (and contains only the necessary) CODE, see fuzzer_simpler.py


import socket
import time
import sys

#Usage:
#python3 fuzzer.py [RHOST] [RPORT] [Max Byte]
#./fuzzer.py [RHOST] [RPORT] [Max Byte]

def usage():
	print("python3 fuzzer.py [RHOST] [RPORT] [Max Byte]")
	print("or")
	print("./fuzzer.py [RHOST] [RPORT] [Max Byte]")
	print("For the second syntax, you should run \"chmod +x fuzzer.py\" in advance.")

if len(sys.argv) < 4:
	print("Wrong Syntax! See usage!")
	usage()
	sys.exit()
elif len(sys.argv) == 4:
	rhost = sys.argv[1]
	rport = int(sys.argv[2])
	max = int(sys.argv[3])
else:
	print("Wrong Syntax! See usage!")
	usage()
	sys.exit()


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
