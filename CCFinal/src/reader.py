import pyshark 
import os
import binascii
import sys
capture = pyshark.LiveCapture(interface='lo', display_filter='http', only_summaries=False)
message=[]
count= 0
for packet in capture.sniff_continuously():
    #GET /c2?4157 HTTP/1.1\r\n
    packet=str(packet)
    try:
        data=packet.split("GET ")[1].split(" ")[0].split("/c")[1].split("?")[0]
        count += 1 
        message.append(data)
        mess=''.join(message)
        if(count==2):
            os.system("clear")
            newmess = binascii.unhexlify(mess).decode()
            print(newmess)
            count = 0
    except:
        continue
capture.close()
exit()
