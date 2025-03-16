
def classify_year(year):
    is_leap = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
    is_huluculu = (year % 15 == 0)
    is_bulukulu = (year % 55 == 0) and is_leap

    if is_leap:
        print("This is leap year.")
    if is_huluculu:
        print("This is huluculu festival year.")
    if is_bulukulu:
        print("This is bulukulu festival year.")
    if not (is_leap or is_huluculu or is_bulukulu):
        print("This is an ordinary year.")
    
def main():
    try:
        while True:
            year =  int(input())
            classify_year(year)
            print()
            
    except EOFError:
        pass
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print