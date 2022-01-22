import socket,sys,getopt

class tcp_server():
    def __init__(self,porto):
        try:
            self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #creacion do socket
            self.server.bind(('',porto)) #asignacion do parametro de entrada de porto ao socket, como se quere que acepte calquiera ip a direccion queda baleira
            self.server.listen() #márcase o socket coma pasivo -> servidor
            while True: #bucle que permite atencion a multiples conexions de clientes
                self.conn,self.address=self.server.accept() #aceptase a conexion
                print(self.address) #mostrase por pantalla a ip
                self.say_hello() #chama o método de saúdo
                
        except KeyboardInterrupt: #pechamos o socket cando se para o programa
            self.server.close()
        except:
            self.manexo_errores() #manexo de erros

    def say_hello(self):
        """envia un saudo ao cliente"""

        mensage = "HTTP/1.0 200 OK\n\nHello World"

        n=self.conn.send((mensage).encode())
        #print(n)    #número de bytes enviados

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