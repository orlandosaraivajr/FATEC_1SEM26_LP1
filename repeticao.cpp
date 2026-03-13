#include <stdio.h>

int main() {
    int soma = 0;
    for(int x=0; x<10;x++) {
        printf("Passando... \n");
        soma = soma + 1;
    }
    printf("\n %i \n\n", soma);
}