import socket,sys,getopt,time,signal,os,threading

class tcp_server():
    def __init__(self,porto):
        try:
            self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #creacion do socket
            self.server.bind(('',porto)) #asignacion do parametro de entrada de porto ao socket, como se quere que acepte calquiera ip a direccion queda baleira
            self.server.listen() #márcase o socket coma pasivo -> servidor

            self.fios = []
            signal.signal(signal.SIGCHLD,self.signal_handler)
            if len(self.fios)==0:
                print("[INFO] creando 3 procesos fios...")
                self.create_fios()
            while len(self.fios)>0: #seguimos executando o servidor mentres queden os fios abertos
                for fio in self.fios:
                    if fio.is_alive()==0: 
                        print("Acabou o fio",fio.name)
                        self.fios.remove(fio) #eliminamos os fios da lista segun van rematando
                pass

        except KeyboardInterrupt: #pechamos o socket cando se para o programa
            self.server.close()

        except OSError:
            self.manexo_errores() #manexo de erros


    def create_fios(self):
        """metodo para crear os fios e poñelos en execucion a espera de clientes"""
        for i in range(3): 
            x = threading.Thread(target=self.funcion_fio, name=i+1) #creacion de fio
            self.fios.append(x)
        print("[INFO] fios creados")
        for fio in self.fios:
            fio.start() #comece de execucion de fio

    def funcion_fio(self):
        """metodo que define a execucion de cada fio"""
        while True:                       
            self.conn,self.address=self.server.accept() #aceptase a conexion
            print("Fio ",threading.current_thread().name) #mostrase o fio por pantalla
            print(self.address) #mostrase por pantalla a ip
            self.say_hello() #chama o método de saúdo
            time.sleep(5)
            self.say_bye() #chama o método de despedida
            exit(0) #esta liña fai que se pechen os fios, se se comenta o servidor segue en execución cos tres fios dispoñibles para atender os clientes


    def say_hello(self):
        """envia un saudo ao cliente"""
        
        n=self.conn.send(("ola que tal").encode())
        #print(n)    #número de bytes enviados

    def say_bye(self):
        """envia unha despedida ao cliente"""
        
        n=self.conn.send(("adeu").encode())
        #print(n)    #número de bytes enviados

    def signal_handler(self, signalNumber,frame):
        pid, status = os.waitpid(0,os.WNOHANG)
        if pid != 0:
            self.fios.remove(pid)
            print("Proceso fillo ", pid, " saiu con estatus ", status)

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