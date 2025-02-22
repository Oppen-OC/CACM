def is_prime(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    
    for i in range(11, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
        
    return True
 
def extendPrime(primes, num):
    aux = primes
    for i in range(len(primes), num+1):
        aux.append(is_prime(i))
    return aux

def fun(x):
    return x*x + x + 41
    
def main():
    primes = []
    
    try:
        while True:
            a, b = input().split(" ")
            a = int(a)
            b = int(b)
            maxV = fun(b)
            if  maxV > len(primes):
                print("Extendmos", len(primes), maxV)
                primes = extendPrime(primes, maxV)
                
            prime = 0
            for i in range(a, b+1):
                if primes[fun(i)]:
                    prime += 1
            print(((prime/ (b-a+1))) * 100)
            
    except EOFError:
        pass
        
if __name__ == "__main__":
    main()
    