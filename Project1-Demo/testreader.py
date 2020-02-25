import pyshark 
import binascii
capture = pyshark.LiveCapture(interface='lo', display_filter='http', only_summaries=True)
message=[]
count= 0
for packet in capture.sniff_continuously():
    temp = packet.info.split()
    if(temp[0]=="GET" and temp[1][1:2]=='c' and temp[1][3:4]=='?'): 
        count += 1 
        message.append(temp[1][2:3])
        mess=''.join(message)
        if(count==2)
            print(binascii.unhexlify(mess).decode().rstrip("\n\-\.\-"), end='')
            count = 0
            mess=''
capture.close()
exit()