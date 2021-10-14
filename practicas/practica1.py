import socket,sys,getopt,binascii

class direccions_IP:
    def __init__(self, host=None, servizo=None, IP=None, porto=None):
        print("***********************************************")
        if host:
            self.host = host
            try:
                self.host_ip()
            except:
                print("O host non existe")
        
        if servizo:
            self.servizo = servizo
            try:
                self.servizo_porto()
            except:
                print("O servizo non existe")

        if IP:
            try:
                socket.inet_pton(socket.AF_INET, IP)
                self.ip = IP
                print("Direccion IPv4 " + self.ip, end=" ") 
                self.ip_host()
            except socket.error:
                try: 
                    socket.inet_pton(socket.AF_INET6, IP)
                    self.ip = IP
                    print("Direccion IPv6 " + self.ip, end=" ")
                    self.ip_host()
                except socket.error:
                    try:
                        self.ip=socket.inet_ntop(socket.AF_INET, binascii.unhexlify(IP))
                        print("Direccion IPv4 " + self.ip, end="")  
                        self.ip_host()
                    except:
                        print("O IP non existe")

        if porto:
            self.porto = porto
            try:
                self.porto_servizo()
            except:
                print("O porto non existe")


        
    def host_ip(self):
        canonico= socket.getaddrinfo(self.host, None, socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_IP,socket.AI_CANONNAME)[0][3]    
        print("Nome canonico: "+ canonico)
        ipv4= socket.getaddrinfo(self.host, None, socket.AF_INET)[0][4][0]
        print("Direccion IPv4: " + ipv4)
        ipv6= socket.getaddrinfo(self.host, None, socket.AF_INET6)[0][4][0]
        print("Direccion IPv6: " + ipv6 )

    def servizo_porto(self):
        porto = socket.getaddrinfo(None, self.servizo)[0][4][1]
        print("Servizo " + self.servizo + ": puerto " + str(porto))

    def ip_host(self):
        host = socket.getnameinfo((self.ip, 0), 0)
        print(": host " + host[0])

    def porto_servizo(self):
        servizo = socket.getnameinfo(("127.0.0.1", int(self.porto)), 0)
        print("Porto " + self.porto + ": servizo " + servizo[1])

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:s:i:p:", ["name","service","ip","port"])
    for opt, arg in opts:
        if opt == '-n':
            direccions_IP(host=arg)
        elif opt == '-s':
            direccions_IP(servizo=arg)
        elif opt == '-i':
            direccions_IP(IP=arg)
        elif opt == '-p':
            direccions_IP(porto=arg)

    if opts==[]:
        print("empty call")
        print("Falta un operando")
        print("Usar: [-n Nombre del host] [-s Nome do servizo (p.e. http)] [-i Direccion ip] [-p Numero de porto]\n")


except:
    print("Falta un operando\nUsar: %s [-n Nombre del host] [-s Nome do servizo (p.e. http)] [-i Direccion ip] [-p Numero de porto]\n")
