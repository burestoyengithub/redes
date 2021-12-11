import socket,sys,getopt,struct

class udp_server():
    def __init__(self,porto):
        try:
            self.reciver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #creacion do socket
            self.reciver.bind(('',porto)) #asignacion do parametro de entrada de porto ao socket
            while True: #bucle que permite atencion a multiples conexions de clientes
                self.mens, self.address = self.reciver.recvfrom(1024) #recepcion de mensaxes de 1024 bytes
                print("Mensaxe:",struct.unpack("d"*(len(self.mens)//8) ,self.mens)) #mostrase por pantalla o mensaxe
                print("Direccion:",self.address,"\n") #mostrase por pantalla a ip e o porto
                
                
        except KeyboardInterrupt: #pechamos o socket cando se para o programa
            self.reciver.close()
        except:
            self.manexo_errores() #manexo de erros

    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""

        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])

try: 
    opts, args = getopt.getopt(sys.argv[1:], "n:p:", ["porto"]) #solicitude de datos por pantalla
    if opts==[]: #execucion de non parametros
        print("Falta un parametro")
        print("Usar: [-p Numero do porto]\n")

    else:
        for opt, arg in opts:
            if opt == '-p':
                udp_server(porto=int(arg))
                
except getopt.GetoptError: #erro de parametros incorrectos
    e = sys.exc_info()[1]
    print(e)
    print("Usar: [-p Numero do porto]\n")

except KeyboardInterrupt: #mensaxe de server apagado
    print("\nServer shutdown")