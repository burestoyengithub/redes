import socket,sys,getopt

class direccions_IP:
    def __init__(self, host=None, servizo=None, IP=None, porto=None):
        if host:
            self.host = host
            try:
                self.host_ip()
            except:
                print("O host non existe")
        
        elif servizo:
            self.servizo = servizo
            print(self.servizo)
            try:
                self.servizo_puerto()
            except:
                print("O servizo non existe")

    def host_ip(self):    
        ipv4= socket.getaddrinfo(self.host, None, socket.AF_INET)[0][4][0]
        print(ipv4)

        ipv6= socket.getaddrinfo(self.host, None, socket.AF_INET6)[0][4][0]
        print(ipv6)

    def servizo_porto(self):
        porto = socket.getaddrinfo("", self.servizo)
        print(porto)



opts, args = getopt.getopt(sys.argv[1:], "n:s:i:p", ["-n","-s","-i","-p"])
    
for opt, arg in opts:
    if opt == '-n':
        direccions_IP(host=arg)
    elif opt == '-s':
        direccions_IP(servizo=arg)
    elif opt == '-i':
        direccions_IP(host=arg)
    elif opt == '-p':
        direccions_IP(host=arg)

