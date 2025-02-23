import sys

def resolver(n, ini, fin):
    # Map each turtle's name to its position in the final stack
    target_pos = {name: i for i, name in enumerate(fin)}

    # Identify the longest correct suffix in ini
    correct_idx = n - 1
    for i in range(n - 1, -1, -1):
        if ini[i] == fin[correct_idx]:
            correct_idx -= 1
        if correct_idx < 0:
            break

    # The turtles to move are the ones before the correct suffix
    turtles_to_move = ini[:correct_idx + 1]

    # Print in the reverse order they appear in the final stack
    for turtle in reversed(fin):
        if turtle in turtles_to_move:
            print(turtle)
    print()  # Blank line between test cases

def main():
    lines = sys.stdin.read().strip().split("\n")
    pointer = 0
    k = int(lines[pointer])  # Number of test cases
    pointer += 1

    for _ in range(k):
        n = int(lines[pointer])  # Stack size
        pointer += 1

        # Read original and final order
        ini = lines[pointer:pointer + n]
        pointer += n
        fin = lines[pointer:pointer + n]
        pointer += n

        resolver(n, ini, fin)

if __name__ == "__main__":
    main()
