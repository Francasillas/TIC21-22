#include <stdio.h>//FICHERO DE CABECERA
int main() {
    float x[10];
    int cont;
    float suma=0;
    float media;
    for(cont=0;cont<10;cont++){//numero empezamos;hasta que numero;de cuanto en cuanto sumamos
    // cont++=cont+1
        printf("dame un numero: ");
        scanf("%f",&x[cont]);
    }
    // EScribo datos en la pantalla
    for(cont=0;cont<10;cont++){
        printf("\n%f",x[cont]);
        suma=suma+x[cont];
        //Suma+=x[cont];
    }
    media=suma/cont;
    printf("\nLa MEDIA VALE= %.2f",media);//%7.2f es como float 7=tamaño campo y 2 decimales. si no sabes lo de la izq = .2
    //donde pone %d ahi saldra lo que queramos que salga
    return (0);
}
