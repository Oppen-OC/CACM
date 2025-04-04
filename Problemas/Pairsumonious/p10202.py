import sys

def reconstruct_numbers(N, sums):
    sums.sort()  # Step 1: Sort the sums to find smallest three sums

    # Step 2: Extract a1, a2, a3 using the three smallest sums
    S1, S2, S3 = sums[0], sums[1], sums[2]


    a1 = (S1 + S2 - S3) // 2  # Using the derived formula
    a2 = S1 - a1
    a3 = S2 - a1

    numbers = [a1, a2, a3]

    # Step 3: Find the rest of the numbers
    index = 3  # Since the first 3 sums are already used
    for _ in range(N - 3):
        new_number = sums[index] - a1  # a1 + a_k = sums[index]
        numbers.append(new_number)
        index += (len(numbers) - 1)  # Move to the next valid sum in the sorted list

    numbers.sort()  # Ensure non-descending order
    print(" ".join(map(str, numbers)))



def main():
    for line in sys.stdin:
        data = list(map(int, line.split()))
        N, sums = data[0], data[1:]
        
        # Check if there are the correct number of sums
        expected_sums_count = (N * (N - 1)) // 2
        if len(sums) != expected_sums_count:
            print("Impossible")
            continue
        
        print(reconstruct_numbers(N, sums))

if __name__ == "__main__":
    main()