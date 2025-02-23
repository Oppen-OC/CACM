
cont = 0



def fun(i, j, p) -> int:
    global cont; cont += 1
    if i == 0: return 1
    elif j == 0: return 0
    elif i < 0 or j < 0:  return -1.0
    else: 
        return p*fun(i-1, j, p) + ((1-p) * fun(i, j-1, p))

def main():
    try:
        while True:
            p, N = input().split(" ")
            for i in range(int(N)):
                global cont; cont = 0
                i, j = input().split(" ")
                res = "{:.5f}".format(fun(int(i), int(j), float(p)))
                print(res)
                print(cont - 1 )
            print()


    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
