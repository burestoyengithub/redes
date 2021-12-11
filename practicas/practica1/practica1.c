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
    int opt;
    // name: Nome do host
    // service: Nome do servizo
    // addr: Direccion IPv4 ou IPv6
    // port: Porto
    char * name = NULL, * service = NULL, * addr = NULL, * port = NULL;

    // Comproba que exista ao menos un operando

    // En caso de erro saimos da función main co codigo EXIT_FAILURE
    if (argc < 2) {
        printf("Falta un operando\n");
        printf("Usar: %s [-n Nombre del host] [-s Nome do servizo (p.e. http)] [-i Direccion ip] [-p Numero de porto]\n", argv[0]);
    return (EXIT_FAILURE);
    }
    // A funcion getopt() permite de forma facil manexar operandos en lina de comandos
    // As opcions n: s: i: p: indican que esos "flags" (nsip) deben de ir seguidos dun argumento
    // Ese parametro gardase na variable externa optarg
    while ((opt = getopt(argc, argv, ":n:s:i:p:")) != -1) {
        switch (opt) {
        case 'n':
            name = optarg; // Argumento nome de host
            break;
        case 's':
            service = optarg; // Argumento nome de servizo
            break;
        case 'i':
            addr = optarg; // Argumento direccion ip
            break;
        case 'p':
            port = optarg; // Argumento numero de porto
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
    // Chamamos as funciones correspondentes aos argumentos solicitados (que son != NULL)
    if (name)
        // Chamar a funcion para obter informacion do host
    if (service)
        // Chamar a funcion para obter informacion do servizo
    if (addr)
        // Chamar a funcion para obter informacion da IP
    if (port)
        // Chamar a funcion para obter informacion do porto
    
    
    printf("****************************************************************\n\n");
    // Finalizamos correctamente, con codigo de saida EXIT_SUCCESS
    return (EXIT_SUCCESS);
}
