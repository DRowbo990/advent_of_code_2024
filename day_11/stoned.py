# Read the input file, split the line into integers, and store them in a list called stones
stones = list(map(int, open("input.txt").readline().strip().split()))

# Initialize an empty dictionary to store computed results for memoization
memory = {}


# Define a recursive function to solve the problem
def solve(stone, blinks):
    """
    Recursively solves the problem based on the given stone value and number of blinks.

    Args:
        stone (int): The initial value of the stone.
        blinks (int): The number of blinks remaining.

    Returns:
        int: The computed result based on the recursive rules.

    The function uses memoization to store previously computed results in the `memory` dictionary
    to avoid redundant calculations. The recursive rules are as follows:
    - If no blinks are left, return 1.
    - If the result for the current (stone, blinks) pair is already computed, return it from memory.
    - If the stone value is 0, recursively solve for stone value 1 with one less blink.
    - If the length of the stone value (as a string) is even, split the stone value into two halves
      and recursively solve for each half with one less blink, then sum the results.
    - If the length of the stone value (as a string) is odd, recursively solve for the stone value
      multiplied by 2024 with one less blink.
    """
    # Base case: if no blinks are left, return 1
    if blinks == 0:
        return 1
    # Check if the result is already computed and stored in memory
    elif (stone, blinks) in memory:
        return memory[(stone, blinks)]
    # If the stone value is 0, recursively solve for stone value 1 with one less blink
    elif stone == 0:
        val = solve(1, blinks - 1)
    # If the length of the stone value (as a string) is even
    elif len(str_stone := str(stone)) % 2 == 0:
        mid = len(str_stone) // 2  # Find the midpoint of the string
        # Recursively solve for the two halves of the stone value with one less blink
        val = solve(int(str_stone[:mid]), blinks - 1) + solve(
            int(str_stone[mid:]), blinks - 1
        )
    # If the length of the stone value (as a string) is odd
    else:
        # Recursively solve for the stone value multiplied by 2024 with one less blink
        val = solve(stone * 2024, blinks - 1)
    # Store the computed result in memory
    memory[(stone, blinks)] = val
    return val


# Compute the sum of results for each stone with 25 blinks and print it
print(sum(solve(stone, 25) for stone in stones))
# Compute the sum of results for each stone with 75 blinks and print it
print(sum(solve(stone, 75) for stone in stones))
