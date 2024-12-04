import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 xmas.py <inputfile>")
    sys.exit(1)

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Read the grid from the input file
with open(input_file, "r") as file:
    grid = [line.strip() for line in file]

# Define the patterns to search for
patterns = [("M", "A", "S"), ("S", "A", "M")]  # MAS  # SAM (backwards MAS)

rows = len(grid)
cols = len(grid[0])


# Function to check if the X-MAS pattern exists starting from (row, col)
def check_xmas(row, col):
    for pattern1 in patterns:
        for pattern2 in patterns:
            # Check the X-MAS pattern
            if (
                row + 2 < rows
                and col + 2 < cols
                and grid[row][col] == pattern1[0]
                and grid[row + 1][col + 1] == pattern1[1]
                and grid[row + 2][col + 2] == pattern1[2]
                and grid[row][col + 2] == pattern2[0]
                and grid[row + 1][col + 1] == pattern2[1]
                and grid[row + 2][col] == pattern2[2]
            ):
                return True
    return False


# Count occurrences of the X-MAS pattern
count = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        if check_xmas(row, col):
            count += 1

# Print the total count of occurrences
print(count)
