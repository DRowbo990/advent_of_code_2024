import sys


def is_safe(columns):
    safe = True
    increasing = (
        None  # None means we haven't determined if it's increasing or decreasing yet
    )

    for i in range(1, len(columns)):
        diff = columns[i] - columns[i - 1]
        if diff == 0 or abs(diff) > 3:
            safe = False
            break
        if increasing is None:
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False
        else:
            if (increasing and diff < 0) or (not increasing and diff > 0):
                safe = False
                break

    return safe


def is_safe_with_dampener(columns):
    if is_safe(columns):
        return True

    for i in range(len(columns)):
        new_columns = columns[:i] + columns[i + 1 :]
        if is_safe(new_columns):
            return True

    return False


tot = 0
# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 levels.py <inputfile>")
    sys.exit(1)

# Get the input file from the command line arguments
input_file = sys.argv[1]

with open(input_file) as file:
    for line in file:
        columns = list(map(int, line.split()))
        if is_safe_with_dampener(columns):
            tot += 1

print(tot)
