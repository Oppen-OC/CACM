import math

def factoriales():
    res = []
    for x in range(7, 14):
        res.append(math.factorial(x))
    return res

def fun(n, res):
    if n < 0:
        if n % 2 == 0:
            print("Underflow!")
        else:
            print("Overflow!")
    elif n < 8:
        print("Underflow!")
    elif n > 13:    
        print("Overflow!")
    else:
        print(res[n-7])
    
        

def main():
    try:
        res = factoriales()
        while True:
            fun(int(input()), res)

    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print