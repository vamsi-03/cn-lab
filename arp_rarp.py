import random
def get_mac():
    f=open("ip.txt","r")
    ipl=[]
    ipl=f.readlines()
    ipn=random.randrange(0,len(ipl))
    ip=ipl[ipn].replace('\n','')
    a = ip.split('.')
    b = hex(int(a[0]))[2:].zfill(2) + hex(int(a[1]))[2:].zfill(2) + hex(int(a[2]))[2:].zfill(2) + hex(int(a[3]))[2:].zfill(2)
    b = b.replace('0x', '')
    b = b.upper()
    mac = '-'.join(b[i: i + 2] for i in range(0, 8, 2))
    f2=open("mac.txt","r")
    macl=[]
    macl=f2.readlines()
    for i in range(len(macl)):
        macl[i]=macl[i].replace('\n','')
        if mac==macl[i]:
            print ("for ip address",ip,"mac address is",mac,"is at the index",i)
        else:
         continue
def get_ip():
    f=open("mac.txt","r")
    macl=[]
    macl=f.readlines()
    macn=random.randrange(0,len(macl))
    mac=macl[macn]
    mac=mac.replace('\n','')
    mac1=mac
    mac=mac.replace('-','')
    octets = [mac[i:i+2] for i in range(0, len(mac), 2)]
    ipn = [int(i, 16) for i in reversed(octets)]
    ipn.reverse()
    ip = '.'.join(str(i) for i in ipn)
    f2=open("ip.txt","r")
    ipl=[]
    ipl=f2.readlines()
    for i in range(len(ipl)):
        ipl[i]=ipl[i].replace('\n','')
        if ip==ipl[i]:
            print("for the mac address",mac1,"ip address is",ip,"found at index",i)
        else:
            continue
if __name__=="__main__":
    print("enter the option \na)ARP\nb)RARP")
    op=input()
    if(op=="a" or op=="A"):
        get_mac()
    elif(op=="b" or op=="B"):
        get_ip()