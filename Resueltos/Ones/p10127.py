def fun(a):
    n = 1
    counter = 1
    while n % a != 0:
        n = n * 10 + 1
        counter += 1
    print(counter)

def main():
    while True:
        try:
            line = input().strip()  # Leer la entrada y eliminar espacios en blanco
            if line == "":  # Si la línea está vacía, terminar
                break
            a = int(line)  # Convertir la entrada a entero
            fun(a)
        except EOFError:
            break  # Terminar el bucle al llegar al final de la entrada

if __name__ == "__main__":
    main()
