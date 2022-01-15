#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    char aux [10];//reservo una variable auxiliar para guardar de momento la palabra
    int longitud;//defino el tamaño
    char*lista[3];
    int cont;
    for (cont=0;cont<3;cont++){
         //1. pido el nombre de un rey
        printf("\n dime el nombre del rey %d: ",cont);
        //2. Lo guardo en una variable auxiliar
        scanf("%s",aux);
        //3. cuento numero de letras
        longitud=strlen(aux);
        //4. busco un hueco en la memoria de ese tamaño y me apunto su direccion
        lista[cont]=(char* )malloc(longitud*sizeof(char));//tamaño de una letra
        //5.copio el nombre desde el auxialiar hasta el hueco enconrado
        strcpy(lista[cont],aux);
    }
    printf("\n los tres reyes magos son: ");
    for (cont=0;cont<3;cont++){
       printf("\n %s",lista[cont]);
    }
    return 0;
}
