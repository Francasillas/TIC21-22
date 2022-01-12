#include <stdio.h>//FICHERO DE CABECERA
int main() {
    int x[10];
    int cont;
    for(cont=0;cont<10;cont++){//numero empezamos;hasta que numero;de cuanto en cuanto sumamos
    // cont++=cont+1
        printf("dame un numero: ");
        scanf("%d",&x[cont]);
    }
    for(cont=0;cont<10;cont++){
        printf("\nx [%d]=%d",cont,x[cont]);
    }
    return (0);
}
