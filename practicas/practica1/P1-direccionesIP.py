import socket,sys,getopt,binascii

class direccions_IP:
    """Clase que recibe un nome de host/nome de servizo/dirección 
    IP/número de porto nos proporcione a información asociada"""

    def __init__(self, host=None, servizo=None, IP=None, porto=None):
        print("***********************************************")
        if host: #en caso de recibir un nome de host chama a funcion de host
            self.host = host
            try:
                self.host_ip() #chamada
            except:
                self.manexo_errores() #funcion de manexo de errores
        
        if servizo:  #en caso de recibir un nome de serbizo chama a funcion de servizo
            self.servizo = servizo
            try:
                self.servizo_porto() #chamada
            except:
                self.manexo_errores() #funcion de manexo de errores

        if IP and porto==None:  #en caso de recibir unha direccion IP chama a funcion de IP
            try: #comprobacion entrada ipv4 como cadea
                socket.inet_pton(socket.AF_INET, IP) 
                self.ip = IP
                print("Direccion IPv4 " + self.ip, end=" ") 
                self.ip_host()
            except:
                try: #comprobacion entrada ipv6 como cadea
                    socket.inet_pton(socket.AF_INET6, IP)
                    self.ip = IP
                    print("Direccion IPv6 " + self.ip, end=" ")
                    self.ip_host()
                except:
                    try: #comprobacion entrada ipv4 como binario
                        self.ip=socket.inet_ntop(socket.AF_INET, binascii.unhexlify(IP))
                        print("Direccion IPv4 " + self.ip, end="")  
                        self.ip_host()
                    except:
                        try: #comprobacion entrada ipv6 como binario
                            self.ip=socket.inet_ntop(socket.AF_INET6, binascii.unhexlify(IP))
                            print("Direccion IPv6 " + self.ip, end="")  
                            self.ip_host()
                        except:
                            self.manexo_errores() #funcion de manexo de errores

        if porto:  #en caso de recibir un numero de porto chama a funcion de porto
            self.ip = IP
            self.porto = porto
            try:
                self.porto_servizo() #chamada
            except:
                self.manexo_errores() #funcion de manexo de errores


        
    def host_ip(self):
        """metodo que recibido unha ip mostra por pantalla toda a información do 
        host, empezando polo nome canónico e seguindo por todas as IPs (v4 y v6) 
        asociadas """

        canonico= socket.getaddrinfo(self.host, None, socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_IP,socket.AI_CANONNAME)[0][3] #nome canonico
        print("Nome canonico: "+ canonico)
        ipv4= socket.getaddrinfo(self.host, None, socket.AF_INET)[0][4][0] #direccion ipv4
        print("Direccion IPv4 en cadea: " + ipv4)
        print("Direccion IPv4 en binario: ", socket.inet_pton(socket.AF_INET,ipv4))

        try: #comprobacion de ipv6
            ipv6= socket.getaddrinfo(self.host, None, socket.AF_INET6)[0][4][0]
            print("Direccion IPv6: " + ipv6 )
            print("Direccion IPv6 en binario: ", socket.inet_pton(socket.AF_INET6,ipv6))
        except:
            self.manexo_errores() #funcion de manexo de errores
            print("O host non ten IPv6")

    def servizo_porto(self):
        """metodo que recibido un servizo mostra por pantalla o porto asociado"""
        porto = socket.getaddrinfo(None, self.servizo)[0][4][1]
        print("Servizo " + self.servizo + ": puerto " + str(porto))

    def ip_host(self):
        """metodo que recibido unha direccion ip mostra por pantalla o host asociado"""
        host = socket.getnameinfo((self.ip, 0), 0)
        print(": host " + host[0])

    def porto_servizo(self):
        """metodo que recibido un numero de porto mostra por pantalla o servizo asociado
        é necesario dar unha ip para ver os servizos, por defecto localhost"""
        servizo = socket.getnameinfo((self.ip if self.ip!=None else "127.0.0.1", int(self.porto)), 0)
        print("Porto " + self.porto + ": servizo " + servizo[1])

    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""
        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])

try: 
    opts, args = getopt.getopt(sys.argv[1:], "n:s:i:p:", ["name","service","ip","port"]) #solicitude de datos por pantalla
    cadena=None #variable para xestionar a opcion de porto con unha ip
    for opt, arg in opts:
        if opt == '-n':
            direccions_IP(host=arg)
        elif opt == '-s':
            direccions_IP(servizo=arg)
        elif opt == '-i':
            cadena=arg
            direccions_IP(IP=arg)
        elif opt == '-p':
            direccions_IP(IP=cadena if cadena else None,porto=arg)

    if opts==[]:
        print("Falta un operando")
        print("Usar: %s [-n Nome do host] [-s Nome do servizo (p.e. http)] [-i Direccion ip] [-p Numero do porto]\n")


except getopt.GetoptError:
    e = sys.exc_info()[1]
    print(e)
    print("Usar: %s [-n Nome do host] [-s Nome do servizo (p.e. http)] [-i Direccion ip] [-p Numero do porto]\n")
