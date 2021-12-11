import socket,sys,getopt

class tcp_client(object):
    def __init__(self, Ip, porto, ficheiro):
        self.saida = open(ficheiro.upper(),"w") #crea un ficheiro saida de 0
        try:
            self.init_socket(Ip,porto)
        except:
            self.manexo_errores() #manexo de erros

        try:
            self.lectura_ficheiro(ficheiro)
        except:
            self.manexo_errores() #manexo de erros
    
        try:
            self.client.close() #peche do socket
            self.r.close() #peche dos ficheiros
            self.saida.close()
        except:
            self.manexo_errores() #manexo de erros

    def init_socket(self, Ip, porto):
        """Crea un socket cliente e o conecta a direccion dada"""    
        self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #crecion do socket
        self.client.connect((Ip,porto)) #conexion co servidor

    def lectura_ficheiro(self, ficheiro):
        """metodo que abre o ficheiro e envia cada linha"""
        self.r = open(ficheiro,"r")
        for linha in self.r:
            self.client.send(linha.encode())
            try:
                self.recepcion()
            except:
                self.manexo_errores() #manexo de erros
            
        
    def recepcion(self):
        "metodo que recibe os datos e os escribe no ficheiro saida"
        datos="s"*1024
        while len(datos)==1024:
            datos=self.client.recv(1024) #recepcion de datos (ata 1024 bytes)
            self.saida.write(datos.decode())
            

    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""

        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])        

try: 
    Ip=None
    opts, args = getopt.getopt(sys.argv[1:], "n:i:p:f:", ["port"]) #solicitude de datos por pantalla

    for opt, arg in opts:
        if opt == '-i':
            Ip=arg
        if opt == '-p':
            porto=arg
        if opt == '-f':
            ficheiro=arg
        
    if porto!=None and Ip!=None and ficheiro!=None: 
        tcp_client(Ip, int(porto), ficheiro)
        
    else: #execucion se non se enviaron os dous parametros
        print("Faltan parametros")
        print("Usar: [-i Direccion IP] [-p Numero do porto] [-f Nome do ficheiro]\n")

except getopt.GetoptError: #erro de parametros incorrectos
    e = sys.exc_info()[1]
    print(e)
    print("Usar: [-i Direccion IP] [-p Numero do porto] [-f Nome do ficheiro]\n")

