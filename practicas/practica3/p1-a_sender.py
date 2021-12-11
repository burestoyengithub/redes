import socket,sys,getopt,struct

class udp_sender():
    def __init__(self,porto_p,Ip,porto_c):
        try:
            self.sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #crecion do socket
            self.sender.bind(('',porto_p)) #asignacion do parametro de entrada de porto propio ao socket
            sended=self.sender.sendto("ola que tal ".encode(),(Ip,porto_c))
            print("Enviaronse",sended,"bytes") 
            self.sender.close() #peche do socket
        except:
            self.manexo_errores() #manexo de erros

    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""

        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])        

try: 
    Ip=None
    opts, args = getopt.getopt(sys.argv[1:], "n:l:i:p:", ["porto local","ip destinatario","porto destinatario"]) #solicitude de datos por pantalla
    pp,Ip,porto=[None]*3
    for opt, arg in opts:
        if opt == '-l':
            pp=arg
        if opt == '-i':
            Ip=arg
        if opt == '-p':
            porto=arg
        
    if porto!=None and Ip!=None and pp!=None: 
        udp_sender(int(pp),Ip,int(porto))
    else: #execucion se non se enviaron os dous parametros
        print("Faltan parametros")
        print("Usar: [-p Numero do porto sender] [-i Direccion IP] [-p Numero do porto reciver]\n")

except getopt.GetoptError: #erro de parametros incorrectos
    e = sys.exc_info()[1]
    print(e)
    print("Usar:[-p Numero do porto sender] [-i Direccion IP] [-p Numero do porto reciver]\n")

