import math

def itera(n, interesante, aburrido):
    cont1 = 1
    cont2 = 0
    aux = n - (n%interesante)
    cont1 = math.floor(n/interesante)

    #print("aux:", aux, "es menor que n:", n)
    #print(aux - (interesante * cont1 + aburrido * cont2))
    aux1 = interesante * cont1
    aux2 = 0
    while(n - (aux1 + aux2) != 0):
        cont1 -= 1
        cont2 += 1
        aux1 -= interesante
        aux2 += aburrido
        if cont1 < 0: return "failed"
    
    return (cont1, cont2)
    
    

def fun(n, box1, box2):
    c1, n1  = map(int, box1.split(" "))
    c2, n2  = map(int, box2.split(" "))
    second = False
    
    if c1/n1 < c2/n2:   # Me interesa quedarme con el primero
        if n % n1 == 0:
            return (n/n1, 0)
        else: 
            return itera(n, n1, n2)
            
        
    else:   # Me interesa quedarme con el segundo
        if n % n2 == 0:
            return (0, n/n2)
        else:
            res =  itera(n, n2, n1)
            if res == "failed": 
                return res
            else: 
                return res[::-1]


def main():
    while True:
        line1 = input()
        if int(line1) == 0:
            return 0
        line2 = input()
        line3 = input()
        #print("n:", line1, ", caja 1:", line2, ", caja2:",line3)
        print(fun(int(line1), line2, line3))

if __name__ == "__main__":
    main()
