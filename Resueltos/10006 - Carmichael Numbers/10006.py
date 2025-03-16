import sys

def prime_sieve(limit=66000):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  
    primes = set()
    
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.add(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return primes

# Precompute all primes
primes = prime_sieve(66000)

carmichael_numbers = {
    561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 
    46657, 52633, 62745, 63973
}

def is_carmichael(N):
    if N in carmichael_numbers:
        return True
    if N in primes or N < 2:  
        return False

    for i in range(2, min(N, 100)):  
        if pow(i, N, N) != i:
            return False
    return True

# Read input
for line in sys.stdin:
    N = int(line.strip())
    if N == 0:
        break

    if is_carmichael(N):
        print(f'The number {N} is a Carmichael number.')
    else:
        print(f'{N} is normal.')
