
def fun(string):
    # Primera linea input()
    print("Hola Mundo:", string)

def main():
    try:
        while True:
            fun(input())
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print