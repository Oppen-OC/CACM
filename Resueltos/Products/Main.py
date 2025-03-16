
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2 

    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # Recursively calculate three multiplications
    z0 = karatsuba(low_x, low_y)         # Low part multiplication
    z1 = karatsuba((low_x + high_x), (low_y + high_y))  # Cross terms
    z2 = karatsuba(high_x, high_y)       # High part multiplication

    # Karatsuba formula: x * y = z2 * 10^(2m) + (z1 - z2 - z0) * 10^m + z0
    return z2 * 10**(2*m) + (z1 - z2 - z0) * 10**m + z0

def main():
    try:
        while True:
            print(karatsuba(int(input()), int(input())))
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print