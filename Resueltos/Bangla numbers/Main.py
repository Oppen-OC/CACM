def solve(money):
    KUTI = 10000000
    LAKH = 100000
    HAJAR = 1000
    SHATA = 100

    if money >= KUTI:
        if money >= KUTI * 100:
            solve(money // (KUTI * 100) * 100)
            money %= KUTI * 100
            if money // KUTI == 0:
                print(" kuti", end="")
            else:
                print(f" {money // KUTI} kuti", end="")
        elif money // KUTI != 0:
            print(f" {money // KUTI} kuti", end="")
        money %= KUTI

    if money >= LAKH:
        if money // LAKH != 0:
            print(f" {money // LAKH} lakh", end="")
        money %= LAKH

    if money >= HAJAR:
        if money // HAJAR != 0:
            print(f" {money // HAJAR} hajar", end="")
        money %= HAJAR

    if money >= SHATA:
        if money // SHATA != 0:
            print(f" {money // SHATA} shata", end="")
        money %= SHATA

    if money != 0:
        print(f" {money}", end="")

def main():
    case_number = 1
    try:
        while True:
            money = input().strip()
            if not money:
                break
            money = int(money)
            print(f"{case_number:4d}.", end="")
            if money != 0:
                solve(money)
            else:
                print(" 0", end="")
            print()
            case_number += 1
    except EOFError:
        pass

if __name__ == "__main__":
    main()
