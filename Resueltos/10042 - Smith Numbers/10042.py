import math

def factorize(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            factors = factorize(n // i)
            factors.append(i)
            return factors
        i += 1
    return [n]

def sum_digits(num):
    total = 0
    while num:
        total += num % 10
        num //= 10
    return total

test_cases = int(input())

for _ in range(test_cases):
    number = int(input())
    number += 1
    while True:
        factors = factorize(number)
        if len(factors) > 1 and sum_digits(number) == sum(sum_digits(f) for f in factors):
            print(number)
            break
        else:
            number += 1
