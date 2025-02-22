#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Función para verificar si un número es primo
bool is_prime(int num) {
    if (num < 2) return false;
    if (num % 2 == 0 || num % 3 == 0 || num % 5 == 0 || num % 7 == 0) 
        return (num == 2 || num == 3 || num == 5 || num == 7);
    
    for (int i = 11; i * i <= num; i += 2) {
        if (num % i == 0)
            return false;
    }
    return true;
}

// Función para extender la lista de primos hasta 'num'
void extendPrime(vector<bool>& primes, int num) {
    int currentSize = primes.size();
    primes.resize(num + 1, false);
    
    for (int i = currentSize; i <= num; i++) {
        primes[i] = is_prime(i);
    }
}

// Función fun(x) = x² + x + 41
int fun(int x) {
    return x * x + x + 41;
}

int main() {
    vector<bool> primes;
    int a, b;
    
    while (cin >> a >> b) {
        int maxV = fun(b);
        
        if (maxV >= primes.size()) {
            cout << "Extendemos " << primes.size() << " hasta " << maxV << endl;
            extendPrime(primes, maxV);
        }

        int primeCount = 0;
        for (int i = a; i <= b; i++) {
            if (primes[fun(i)]) {
                primeCount++;
            }
        }

        double percentage = (double)primeCount / (b - a + 1) * 100;
        printf("%.2f\n", percentage);
    }

    return 0;
}
