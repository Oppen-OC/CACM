import math

def multinomial_coefficient(n, poli):
    numerator = math.factorial(n)
    denominator = 1
    for num in poli:
        denominator *= math.factorial(num)
    return numerator // denominator  # Integer division

def main():
    while True:
        try:
            line = input().strip()
            if not line:  # Check if line is empty
                break
            
            n, k = map(int, line.split())  # Extract n and k
            poli = list(map(int, input().split()))  # Read k values
            
            print(multinomial_coefficient(n, poli))  # Compute and print result
        except EOFError:
            break  # Stop when input ends
        except ValueError:
            print("Invalid input")
            break

if __name__ == "__main__":
    main()
