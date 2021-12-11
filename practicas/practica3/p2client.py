import socket,sys,getopt

class ucp_client(object):
    def __init__(self,porto_p, Ip, porto_s, ficheiro):
        self.saida = open(ficheiro.upper(),"w") #crea un ficheiro saida de 0
        try:
            self.init_socket(porto_p) #inicalizacion do socket
        except:
            self.manexo_errores() #manexo de erros

        try:
            self.lectura_ficheiro(Ip,porto_s,ficheiro)
        except:
            self.manexo_errores() #manexo de erros
    
        try:
            self.client.close() #peche do socket
            self.r.close() #peche dos ficheiros
            self.saida.close()
        except:
            self.manexo_errores() #manexo de erros

    def init_socket(self, porto_p):
        """Crea un socket cliente """    
        self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #crecion do socket
        self.client.bind(('',porto_p)) #asignacion do parametro de entrada de porto propio ao socket

    def lectura_ficheiro(self,Ip, porto_s, ficheiro):
        """metodo que abre o ficheiro e envia cada linha"""
        self.r = open(ficheiro,"r")
        for linha in self.r:
            sended = self.client.sendto(linha.encode(),(Ip,porto_s)) #envio de cada liña
            print("Enviaronse",sended,"bytes") 
            try:
                self.recepcion()
            except:
                self.manexo_errores() #manexo de erros
            
        
    def recepcion(self):
        "metodo que recibe os datos e os escribe no ficheiro saida"

        datos, address = self.client.recvfrom(1024) #recepcion de datos (ata 1024 bytes)
        print("Recibidoa",len(datos),"bytes de",address)
        self.saida.write(datos.decode())
            

    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""

        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])

try: 
    Ip=None
    opts, args = getopt.getopt(sys.argv[1:], "n:l:i:p:f:", ["porto local","ip destinatario","porto destinatario","ficheiro"]) #solicitude de datos por pantalla
    pp,Ip,porto,ficheiro=[None]*4
    for opt, arg in opts:
        if opt == '-l':
            pp=arg
        if opt == '-i':
            Ip=arg
        if opt == '-p':
            porto=arg
        if opt == '-f':
            ficheiro=arg
        
    if porto!=None and Ip!=None and ficheiro!=None and pp!=None: 
        ucp_client(int(pp), Ip, int(porto), ficheiro)
        
    else: #execucion se non se enviaron os dous parametros
        print("Faltan parametros")
        print("Usar: [-p Numero do porto cliente]  [-i Direccion IP] [-p Numero do porto servidor] [-f Nome do ficheiro]\n")

except getopt.GetoptError: #erro de parametros incorrectos
    e = sys.exc_info()[1]
    print(e)
    print("Usar: [-p Numero do porto cliente] [-i Direccion IP] [-p Numero do porto servidor] [-f Nome do ficheiro]\n")

