import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 levels.py <inputfile>")
    sys.exit(1)

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Open the file in read mode
with open(input_file, "r") as file:
    tot = 0
    for line in file:
        columns = list(map(int, line.split()))
        safe = True
        increasing = None  # None means we haven't determined if it's increasing or decreasing yet

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

        if safe:
            tot += 1

print(tot)
