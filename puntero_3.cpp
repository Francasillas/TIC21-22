#include <stdio.h>
#include<string.h>
#include<stdlib.h>//malloc
//puntero 3 RESERVA DINAMICA DE MEMORIA  
int main() {
    char aux[100]; //reservo una variable aux para guardar de momento una palabra
    int longitud; //defino el tamaño palabra
    printf("\n Dime una palabra: ");
    scanf("%s",aux); //leo palabra
    longitud= strlen(aux);  
    char *palabra; //palabra es un puntero( una variable q contiene una direccion de memoria de algo que es una letra)
    palabra=(char*) malloc(longitud*sizeof(char)); //si es una palabra poner siempre (CHAR*) si es num(int*)  //memory allocation = reserva de memoria = localizar tmñ memoria y guardarlo
    strcpy(palabra,aux); //copia letra a letra una palabra
    printf("\n RESULTADO: ");
    printf("%s", palabra);
    return (0);
