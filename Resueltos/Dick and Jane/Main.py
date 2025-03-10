import math

def fun(s, p, y, j):
    Y = (12 + j - p - y) // 3

    if (12 + j - p - y) % 3 == 0:
        print(y + Y, p + Y, Y)
    elif (12 + j - p - y) % 3 == 1:
        if p + s == y:
            print(y + Y + 1, p + Y, Y)
        else:
            print(y + Y, p + Y + 1, Y)
    else:
        print(y + Y + 1, p + Y + 1, Y)

def main():
    try:
        while True:
            line = list(map(int, input().split(" ")))
            # Spot tenia s años cuando nació Puff
            # Puff tenia p años cuando nació Yertle
            # Spot tenia y años cuando nació Yertle
            # La suma de Spot, Puff y Yertle es la suma de las edades de Dick y Jane.
            fun(line[0], line[1], line[2], line[3])
            # Devuelve la edad de Spot, Puff y Yertle
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print