#include <stdio.h>
#include <stdlib.h>

int* itera(int n, int interesante, int aburrido) {
    int cont1 = 1;
    int cont2 = 0;
    int aux = interesante;
    static int result[2];
    
    while (aux < n - interesante) {
        aux += interesante;
        cont1 += 1;
    }
    
    while (n - (interesante * cont1 + aburrido * cont2) != 0) {
        cont1 -= 1;
        cont2 += 1;
        if (cont1 < 0) {
            return NULL;
        }
    }
    
    result[0] = cont1;
    result[1] = cont2;
    return result;
}

void fun(int n, int c1, int n1, int c2, int n2) {
    int* res;
    
    if ((double)c1 / n1 < (double)c2 / n2) { // Prefiero el primero
        if (n % n1 == 0) {
            printf("(%d, 0)\n", n / n1);
            return;
        } else {
            res = itera(n, n1, n2);
        }
    } else { // Prefiero el segundo
        if (n % n2 == 0) {
            printf("(0, %d)\n", n / n2);
            return;
        } else {
            res = itera(n, n2, n1);
            if (res == NULL) {
                printf("failed\n");
                return;
            } else {
                printf("(%d, %d)\n", res[1], res[0]);
                return;
            }
        }
    }
    
    if (res == NULL) {
        printf("failed\n");
    } else {
        printf("(%d, %d)\n", res[0], res[1]);
    }
}

int main() {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) return 0;
        
        int c1, n1, c2, n2;
        scanf("%d %d", &c1, &n1);
        scanf("%d %d", &c2, &n2);
        
        fun(n, c1, n1, c2, n2);
    }
    
    return 0;
}
