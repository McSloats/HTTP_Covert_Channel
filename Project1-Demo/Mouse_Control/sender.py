import binascii
import sys
import time
import subprocess

def transmit_msg():
	#Convert TEXT file to HEX
	with open(sys.argv[1], 'rb') as f:
		message = f.read()
	message = str(binascii.hexlify(message), 'utf-8')
	print("Number of bytes: "+str(len(message)))
	print("Message: "+message)
	#Write out HEX to new TMP file
	tmp_file = open("tmp.txt","a")
	tmp_file.write(message)
	tmp_file.close()
	execution = time.time()

	#Execute bash script
	subprocess.run(["./mouse-control", "tmp.txt"])
	subprocess.run(["rm", "tmp.txt"])
	execution = (time.time() - execution)
	
	print(execution)

transmit_msg()
