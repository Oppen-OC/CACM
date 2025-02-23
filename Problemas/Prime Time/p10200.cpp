#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

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

void extendPrime(vector<bool>& primes, int num) {
    int currentSize = primes.size();
    primes.resize(num + 1, false);
    
    for (int i = currentSize; i <= num; i++) {
        primes[i] = is_prime(i);
    }
}

int fun(int x) {
    return x * x + x + 41;
}

int main(int argc, char* argv[]) {

    string inputFileName = argv[1];
    string outputFileName = argv[2];

    ifstream inputFile(inputFileName);
    ofstream outputFile(outputFileName);

    vector<bool> primes;
    int a, b;

    while (inputFile >> a >> b) {
        int maxV = fun(b);
        
        if (maxV >= primes.size()) {
            extendPrime(primes, maxV);
        }

        int primeCount = 0;
        for (int i = a; i <= b; i++) {
            if (primes[fun(i)]) {
                primeCount++;
            }
        }

        double percentage = (double)primeCount / (b - a + 1) * 100;
        outputFile << fixed;
        outputFile.precision(2);
        outputFile << percentage << endl;
    }

    inputFile.close();
    outputFile.close();
    return 0;
}
