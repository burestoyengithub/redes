import socket,sys,getopt,binascii,ipaddress,time


class router(object):
    def __init__(self,taboa,ip=None,tempo_ex=True):
        self.dict_ip_int={} #creacion dun dicionario onde se vai a almacear a taboa
        try:
            self.lectura_ficheiro(taboa) #lectura do ficheiro
        except:
            self.manexo_errores() #manexo de erros

        if ip==None:
            try:
                for rede in self.dict_ip_int:
                    self.info_red(rede) #info da rede se non hai ip de entrada
            except:
                self.manexo_errores() #manexo de erros

        else: #interface de saida si hai entrada de ip
            try:
                print("\nResultados metodo in:")
                start=time.time()
                self.redic_in(ip) #metodo in
                in_t=time.time()-start
                if tempo_ex:
                    print("\nResultados metodo aritmetico:")
                    start=time.time()
                    self.redic_arit(ip) #metodo aritmetico
                    arit_t=time.time()-start
                    print("\nTiempo in:",in_t,"\nTiempo arit",arit_t) #mostra de resultados temporales
            except:
                self.manexo_errores() #manexo de erros
        
    def lectura_ficheiro(self, ficheiro):
        """metodo que abre o ficheiro e gardo os datos nun dicionario"""
        self.r = open(ficheiro,"r") #apertura de ficheiro
        for linha in self.r: 
            ip,interface = linha.split(",") #separacion entre direccion e interface
            self.dict_ip_int[ipaddress.ip_network(ip,False)]=interface #asignacion o dicionario
            
    def info_red(self,rede):
        """metodo que recibida unha rede mostra a sua direccion, mascara, lonxitude de prefixo, rango de direccións e interface"""
        print(rede) #mostra de datos de pantalla
        print("\tDireccion de rede",rede)
        print("\tMascara de rede",rede.netmask) 
        print("\tLonxitude de prefixo",rede.prefixlen)
        print("\tNúmero de direccions",rede.num_addresses)
        print("\tPrimeira direccion:",rede.network_address,"Última direccion:",rede.broadcast_address)
        print("\tInterface",self.dict_ip_int[rede],"\n")
        
    def redic_in(self,ip):
        """metodo que comproba a interface de saida dunha direccion de entrada mediante o metodo in"""
        ip_ad=ipaddress.ip_address(ip)
        coinc={rede:rede.prefixlen for rede in list(self.dict_ip_int) if ip_ad in rede} #creacion dun novo dicionario cos valores coincidentes e lonxitudes de prefixo
        if len(coinc)>0: #no caso de que a direccion de entrada este contido nalguna rede da taboa de renvio
            red_max = max(coinc, key=coinc.get) #obtemos o valor do prefixo máis alto (regra prefixo)
            print("Rede:",red_max,"\nInterface:",self.dict_ip_int[red_max],"\nBits de prefixo:",coinc[red_max]) #mostra por pantalla de resultados
        else:
            print("Interface(por defecto no coincidencias) -> 0") #no caso de non haber coindidencias a interface de saida e a 0

    def redic_arit(self,ip):
        """metodo que comproba a interface de saida dunha direccion de entrada mediante o metodo aritmetico"""
        ip_ad=ipaddress.ip_address(ip)
        coinc={rede:rede.prefixlen for rede in list(self.dict_ip_int) if (int(ip_ad) - int(rede[0])) >= 0} #creacion dun novo dicionario cos valores coincidentes e lonxitudes de prefixo
        if len(coinc)>0: #no caso de que a direccion de entrada este contido nalguna rede da taboa de renvio
            red_max = max(coinc, key=coinc.get) #obtemos o valor do prefixo máis alto (regra prefixo)
            print("Rede:",red_max,"\nInterface:",self.dict_ip_int[red_max],"\nBits de prefixo:",coinc[red_max]) #mostra por pantalla de resultados
        else:
            print("Interface(por defecto no coincidencias) -> 0") #no caso de non haber coindidencias a interface de saida e a 0

    def manexo_errores(self):
        """metodo que se chama cando salta un erro mostra por pantalla o nome do erro
        e a que se debe"""

        e = sys.exc_info()
        print("Nome de error: ",e[0].__name__)
        print("Explicacion de error: ",e[1])
try: 
    opts, args = getopt.getopt(sys.argv[1:], "t:i:m", ["arquivo da taboa","ip","opcion de medicion de tempos"]) #solicitude de datos por pantalla
    ip_data=None
    medida=True
    for opt, arg in opts:
        if opt == '-t':     
            taboa=arg

        elif opt == '-i':
            ip_data = arg

        elif opt == '-m':
            medida=arg
        
    router(taboa,ip=ip_data,tempo_ex=medida) #chaamada a clase cos valores de entrada

except:
    e = sys.exc_info()[1]
    print("A opcion de arquivo de taboa é obligatoria")
    print(e)
    print("Usar: %s [-t arquivo da taboa] [-i direccionn ip] [-m opcion de medicion de tempos]\n")
