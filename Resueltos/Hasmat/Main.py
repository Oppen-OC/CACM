import math

def fun(x, y):
    print(int(math.fabs(y - x)))

def main():
    try:
        while True:
            x, y = tuple(map(int, input(). split()))
            fun(x,y)
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print