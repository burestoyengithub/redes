import socket,sys,getopt

class tcp_client():
    def __init__(self,Ip,porto):
        try:
            self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #crecion do socket
            self.client.connect((Ip,porto)) #conexion co servidor
        
            datos=self.client.recv(1024) #recepcion de datos (ata 1024 bytes)
            print("Chegaron", len(datos),"bytes ->", datos.decode()) #xa que cada letra e un byte a lonxitude dos bytes recibidos e len(datos)
            datos=self.client.recv(1024) #recepcion de datos (ata 1024 bytes)
            print("Chegaron", len(datos),"bytes ->", datos.decode()) #xa que cada letra e un byte a lonxitude dos bytes recibidos e len(datos)
            self.client.close() #peche do socket
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
    porto=None
    opts, args = getopt.getopt(sys.argv[1:], "n:i:p:", ["port"]) #solicitude de datos por pantalla

    for opt, arg in opts:
        if opt == '-i':
            Ip=arg
        if opt == '-p':
            porto=arg
        
    if porto!=None and Ip!=None: 
        tcp_client(Ip,porto=int(porto))
    else: #execucion se non se enviaron os dous parametros
        print("Faltan parametros")
        print("Usar: [-i Direccion IP] [-p Numero do porto]\n")

except getopt.GetoptError: #erro de parametros incorrectos
    e = sys.exc_info()[1]
    print(e)
    print("Usar: [-i Direccion IP] [-p Numero do porto]\n")

