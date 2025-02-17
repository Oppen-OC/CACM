import time

def fun():
    print("Ingrese un número: ")

    x = int(input()) 
    y = 0
    yF = 0

    matrix = [0]*x
    initialF = time.time()
    for i in range(1, x):
        x = i
        initial = time.time()
        while(x != 1):
            y += 1
            if(x % 2 == 0):
                x = x / 2
            else:
                x = 3 * x + 1
        yF += y
        final = time.time()

    matrix[i] = (y, (final-initial)* 1000)
    finalF = time.time()

    print("Ejecución terminada con y = ", matrix)
    print("Ejecución terminada con y = ", (finalF - initialF)*1000, "ms")
    
def test():
    print("Introduce numero: ")
    x = int(input()) 
    y = 0
    initial = time.time()
    while(x != 1):
        y += 1
        if(x % 2 == 0):
            x = x / 2
        else:
            x = 3 * x + 1
    final = time.time()
    print("Ejecución terminada con y = ", (final - initial)*1000, "ms")

def main():
    fun()
    #test()
    
if __name__ == "__main__":
    main()