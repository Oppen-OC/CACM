
def fun():
    # Primera linea input()
    print("Hola Mundo")

def main():
    try:
        while True:
            input()
            fun()
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print
    
    # Esta vaina era sumar delta e ir cambiado su valor cada k veces o algo asi
    # No se que es delta, lmao