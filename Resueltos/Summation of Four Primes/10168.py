import sys

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(4, limit + 1, 2):
        is_prime[i] = False
    for i in range(3, int(limit ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return is_prime, primes

limit = 10000000
is_prime, primes = sieve_of_eratosthenes(limit)

for line in sys.stdin:
    n = int(line.strip())
    if n < 8:
        print("Impossible.")
    else:
        if n % 2 == 0:
            a, b = 2, 2
        else:
            a, b = 2, 3
        s = n - (a + b)
        for i in primes:
            if i >= s:
                break
            if is_prime[s - i]:
                print(a, b, i, s - i)
                break
        else:
            print("Impossible.")
