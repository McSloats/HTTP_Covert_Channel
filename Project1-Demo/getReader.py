import pyshark 
capture = pyshark.LiveCapture(interface='lo0', display_filter='http', only_summaries=True)
message=[]
check=[]
start = False
for packet in capture.sniff_continuously():
    if(not start):
        temp = packet.info.split()
        if(temp[0]=="GET"):
            check.append(temp[1][2:3])
        if(len(check)==6): 
            end = ''.join(check)
            if(end=='2D2E2D'): 
                start=True 
            else: 
                check=[]
    else: 
        if(temp[0]=="GET" and temp[1][1:2]=='c' and temp[1][3:4]=='?'): 
            if(len(check)==6): 
                end = ''.join(check)
                #print(end)
                if(end=='2D2E2D'): 
                    mess=''.join(message)
                    print(mess.decode("hex"))
                    break 
                else: 
                    check=[]
            check.append(temp[1][2:3])
            message.append(temp[1][2:3])
    