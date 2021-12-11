import socket,sys,getopt

class tcp_server():
    def __init__(self,porto):
        try:
            self.init_socket(porto)
        except:
            self.manexo_errores() #manexo de erros

        try:
            self.escoita()
        except KeyboardInterrupt: #pechamos o socket cando se para o programa
            self.server.close()
        except:
            print("mal")
            self.manexo_errores() #manexo de erros
        
    def init_socket(self, porto):
        self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #creacion do socket
        self.server.bind(('',porto)) #asignacion do parametro de entrada de porto ao socket, como se quere que acepte calquiera ip a direccion queda baleira
        self.server.listen() #márcase o socket coma pasivo -> servidor

    def escoita(self):
        """metodo que permite atencion a multiples conexions de clientes"""
        while True: 
            self.conn,self.address=self.server.accept() #aceptase a conexion
            print(self.address) #mostrase por pantalla a ip
            while True:
                try:
                    DATOS = self.recepcion()
                    
                except:
                    self.manexo_errores() #manexo de erros
                if DATOS!="":
                    try:
                        self.conn.send(DATOS.encode())
                    except:
                        self.manexo_errores() #manexo de erros
                else:
                    break



    def recepcion(self):
        "metodo que recibe os datos e os devolve en mayusculas"
        recibido="s"*1024
        datos=""
        while len(recibido)==1024:
            recibido=self.conn.recv(1024) #recepcion de datos (ata 1024 bytes)
            datos+=recibido.decode()
        return datos.upper()


    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""

        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])

try: 
    opts, args = getopt.getopt(sys.argv[1:], "n:p:", ["port"]) #solicitude de datos por pantalla
    if opts==[]: #execucion de non parametros
        print("Falta un parametro")
        print("Usar: [-p Numero do porto]\n")

    else:
        for opt, arg in opts:
            if opt == '-p':
                tcp_server(porto=int(arg))
                
except getopt.GetoptError: #erro de parametros incorrectos
    e = sys.exc_info()[1]
    print(e)
    print("Usar: [-p Numero do porto]\n")

except KeyboardInterrupt: #mensaxe de server apagado
    print("\nServer shutdown")