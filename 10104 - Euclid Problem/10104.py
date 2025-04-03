import sys


def calculate_factors(a, b):
    prev_x, prev_y = 1, 0
    x, y = 0, 1

    while b:
        quotient = a // b
        a, b = b, a % b
        prev_x, x = x, prev_x - quotient * x
        prev_y, y = y, prev_y - quotient * y

    return a, prev_x, prev_y


def process_input():
    try:
        for line in sys.stdin:
            values = list(map(int, line.strip().split()))
            if len(values) == 2:
                num1, num2 = values
                gcd_result, factor1, factor2 = calculate_factors(num1, num2)
                print(factor1, factor2, gcd_result)
    except EOFError:
        pass

    sys.exit(0)


if __name__ == "__main__":
    process_input()
