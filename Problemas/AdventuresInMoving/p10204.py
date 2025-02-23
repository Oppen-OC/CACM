def perm(w1, h1, l1):
    # Permutaciones posibles de la caja
    # ancho del suelo, largo del suelo y altura
    p = []
    p.append([w1, h1, l1])
    p.append([w1, l1, h1])
    p.append([h1, w1, l1])
    p.append([h1, l1, w1])
    p.append([l1, w1, h1])
    p.append([l1, h1, w1])
    return p

import math

import math

def fits_through_door(w, h, H):
    """Check if a box with width `w` and height `h` can fit through a door of height `H`, allowing tilting."""
    if h <= H:  
        return True  # Fits without tilting
    diagonal = math.sqrt(w**2 + h**2)  # Tilted height
    return diagonal <= H  # Check if diagonal tilt fits

def cargar(w0, h0, l0, H, w1, h1, l1):
    """Check if the box can be loaded into the truck."""
    for bw, bh, bl in perm(w1, h1, l1):  # Try all orientations
        # Check if it can pass through the door in at least one orientation
        if fits_through_door(bw, bh, H) or fits_through_door(bl, bh, H):
            # Check if the box fits inside the truck once placed
            if bw <= w0 and bh <= h0 and bl <= l0:
                return True  # The box fits

    return False  # No valid orientation works




    
def fun(w0, h0, l0, H, w1, h1, l1):
    permutaciones = perm(w1, h1, l1)
    if w1 > H and h1 > H and l1 > H:
        print("The box will not go on the truck.")
        return
    else:
        for p in permutaciones:
            if cargar(w0, h0, l0, H, p[0], p[1], p[2]):
                print("The box goes on the truck.")
                return
        print("The box will not go on the truck.")
        

def main():
    try:
        while True:
            # Convertir todas las entradas a enteros
            car = list(map(int, input().split()))
            box = list(map(int, input().split()))

            w0 = car[0]; h0 = car[1]; l0 = car[2]; H = car[3]    
            w1 = box[0]; h1 = box[1]; l1 = box[2]

            fun(w0, h0, l0, H, w1, h1, l1)

    except EOFError:
        pass
    
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con printº