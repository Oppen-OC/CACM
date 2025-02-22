import sys
from itertools import combinations

def is_valid_solution(nums, target_sums):
    """Check if the given list of nums produces the target sums."""
    current_sums = sorted(x + y for x, y in combinations(nums, 2))
    return current_sums == target_sums

def backtrack(nums, remaining_sums, N):
    """Backtracking function to find a valid sequence of N numbers."""
    if len(nums) == N:
        # If we have N numbers, check if they generate the correct sums
        if is_valid_solution(nums, remaining_sums):
            return nums
        return None
    
    # Next number should be consistent with existing sums
    last_num = nums[-1]
    used = set()
    
    for s in remaining_sums:
        # Try to deduce the next number from any remaining sum
        candidate = s - last_num
        
        if candidate in used or candidate < last_num:
            continue
        
        # Check if this candidate is compatible with existing numbers
        new_sums = [candidate + num for num in nums]
        
        # Ensure these new sums exist in the remaining sums
        if all(new_sum in remaining_sums for new_sum in new_sums):
            # Backtrack with new number
            new_remaining_sums = remaining_sums.copy()
            for new_sum in new_sums:
                new_remaining_sums.remove(new_sum)
                
            solution = backtrack(nums + [candidate], new_remaining_sums, N)
            if solution:
                return solution
            used.add(candidate)
    
    return None

def solve_case(N, sums):
    """Solve a single test case."""
    sums.sort()
    
    # Derive the first three numbers using the smallest three sums
    a1 = (sums[0] + sums[1] - sums[2]) // 2
    a2 = sums[0] - a1
    a3 = sums[1] - a1
    
    # Initial state of the backtracking
    initial_nums = [a1, a2, a3]
    initial_sums = sums.copy()
    
    # Remove the sums for the initial three numbers
    initial_sums.remove(a1 + a2)
    initial_sums.remove(a1 + a3)
    initial_sums.remove(a2 + a3)
    
    # Use backtracking to find the full set of numbers
    result = backtrack(initial_nums, initial_sums, N)
    
    if result:
        print(" ".join(map(str, sorted(result))))
    else:
        print("Impossible")

def main():
    input = sys.stdin.read().strip().splitlines()
    for line in input:
        data = list(map(int, line.split()))
        N = data[0]
        sums = data[1:]
        
        if len(sums) != (N * (N - 1)) // 2:
            print("Impossible")
            continue
        
        solve_case(N, sums)

if __name__ == "__main__":
    main()
