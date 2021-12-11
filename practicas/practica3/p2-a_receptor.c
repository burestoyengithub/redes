#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <inttypes.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
#include <string.h>



int main(int argc, char * argv[]) {
    int opt, socket_c, ret, port, recv_len;
    struct sockaddr_in servaddr, sother;
    // ip: Direccion Ip
    // porto: Nome do porto
    char * ip = NULL, * porto = NULL;
    // Comproba que exista ao menos un operando

    // En caso de erro saimos da función main co codigo EXIT_FAILURE
    if (argc < 2) {
        printf("Falta un operando\n");
        printf("Usar: %s [-p Numero de porto]\n", argv[0]);
    return (EXIT_FAILURE);
    }
    // A funcion getopt() permite de forma facil manexar operandos en lina de comandos
    // As opcions i: p: indican que esos "flags" (ip) deben de ir seguidos dun argumento
    // Ese parametro gardase na variable externa optarg
    while ((opt = getopt(argc, argv, ":p:")) != -1) {
        switch (opt) {  
        case 'p':
            porto = optarg; // Argumento numero de porto
            break;
        case ':': // Intruduciuse un flag sen argumento obligatorio
            fprintf(stderr, "A opción -%c require un argumento.\n", optopt);
            return (EXIT_FAILURE);
            break;
        case '?':
            if (isprint(optopt)) // Intruduciuse un flag incorrecto
                fprintf(stderr, "Opción descoñecida `-%c'.\n", optopt);
            else // Hai un caracter non lexible nas opcions
                fprintf(stderr, "Caracter de opción descoñecido `\\x%x'.\n", optopt);
            return (EXIT_FAILURE);
            break;
        default: // Produciuse un erro indeterminado. Nunca se deberia chegar aqui.
        abort();
        }
    }
    
    printf("\n");
    // Ponse o cliente a funcionar se se introduciron os datos de ip e portp
    if (porto){
        port = atoi(porto);
        // creacion del socket
        socket_c = socket(AF_INET, SOCK_DGRAM, 0);
        if (socket_c == -1) {
            printf("fallo ó crear o socket\n");
            return (EXIT_FAILURE);
        }

        servaddr.sin_family = AF_INET;
        servaddr.sin_addr.s_addr = htons(INADDR_ANY);
        servaddr.sin_port = htons(port);

        // asignacion de porto
        if(bind(socket_c, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0){
            printf("Fallou a asignacion \n");
            return (EXIT_FAILURE);
        }
        else{
            printf("esperando datos\n");
        }
        while(1){
            // recepcion de datos
            char buf[1024];
            int len = sizeof(sother);
            if ((recv_len = recvfrom(socket_c, (char *)buf, 1024, 0, (struct sockaddr *) &sother, &len)) == -1)
            {
                printf("Falllou a recepcion");
                return (EXIT_FAILURE);
            }
            
            //mostra de recepcion
            printf("Recibidos %i bytes de %s:%d\n", len, inet_ntoa(sother.sin_addr), ntohs(sother.sin_port));
            printf("Mensaxe: %s\n" ,buf);
            }
        close(socket_c);
        return (EXIT_SUCCESS);}
}


	