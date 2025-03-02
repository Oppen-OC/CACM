
def fun(a, b):
    # Primera linea input()
    print("Hola Mundo")

def main():
    try:
        while True:
            a, b= input().split(" ")
            fun(int(a), int(b))
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print