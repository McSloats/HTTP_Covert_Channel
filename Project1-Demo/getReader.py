import pyshark 
import binascii
capture = pyshark.LiveCapture(interface='lo', display_filter='http', only_summaries=True)
message=[]
check=[]
start = False
end = '000000'
for packet in capture.sniff_continuously():
    temp = packet.info.split()
    if(not start):
        if(temp[0]=="GET"):
            check.append(temp[1][2:3])
        if(len(check)==5): 
            end = ''.join(check)
            if(end=='D2D2D'): 
                start=True
                check=[]
            else: 
                check=[]
    else:
        if(temp[0]=="GET" and temp[1][1:2]=='c' and temp[1][3:4]=='?'): 
            if(len(check)==6): 
                 end = ''.join(check)
                 if(end=='2D2E2D'):
                     mess=''.join(message)
                     print(binascii.unhexlify(mess).decode().rstrip("\n\-\.\-"))
                     break
                 else: 
                     check=check[1:]
            #else:
            check.append(temp[1][2:3])
            message.append(temp[1][2:3])
capture.close()
exit()
