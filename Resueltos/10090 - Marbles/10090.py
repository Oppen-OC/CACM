import sys
import math


def find_coefficients(num1, num2):
    a, b = 0, 1
    prev_a, prev_b = 1, 0
    while num2:
        quotient = num1 // num2
        num1, num2 = num2, num1 % num2
        a, prev_a = prev_a - quotient * a, a
        b, prev_b = prev_b - quotient * b, b
    return num1, prev_a, prev_b


def optimize_boxes(items, costX, capacityX, costY, capacityY):
    divisor, coefX, coefY = find_coefficients(capacityX, capacityY)

    if items % divisor != 0:
        print("failed")
        return

    coefX *= items // divisor
    coefY *= items // divisor

    stepA = capacityY // divisor
    stepB = capacityX // divisor

    lower_bound = math.ceil(-coefX / stepA)
    upper_bound = math.floor(coefY / stepB)

    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)

    if lower_bound > upper_bound:
        print("failed")
        return

    best_choice = lower_bound if costX * stepA > costY * stepB else upper_bound

    coefX += best_choice * stepA
    coefY -= best_choice * stepB

    print(coefX, coefY)


def main():
    try:
        while True:
            items = int(input().strip())
            if items == 0:
                break
            costX, capacityX = map(int, input().strip().split())
            costY, capacityY = map(int, input().strip().split())
            optimize_boxes(items, costX, capacityX, costY, capacityY)
    except EOFError:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
