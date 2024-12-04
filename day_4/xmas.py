import sys  # Import the sys module for command line arguments
import re  # Import the re module for regular expressions

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 mul.py <inputfile>")  # Print usage message
    sys.exit(1)  # Exit the program with an error code

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Read the grid from the input file
with open(input_file, "r") as file:
    grid = [line.strip() for line in file]

# Define the word to search for
word = "XMAS"
word_len = len(word)
rows = len(grid)
cols = len(grid[0])


# Function to check if the word exists starting from (row, col) in a given direction
def check_word(row, col, delta_row, delta_col):
    for i in range(word_len):
        r = row + i * delta_row
        c = col + i * delta_col
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
            return False
    return True


# Count occurrences of the word in all directions
count = 0
for row in range(rows):
    for col in range(cols):
        # Check all 8 possible directions
        if check_word(row, col, 0, 1):  # Horizontal right
            count += 1
        if check_word(row, col, 0, -1):  # Horizontal left
            count += 1
        if check_word(row, col, 1, 0):  # Vertical down
            count += 1
        if check_word(row, col, -1, 0):  # Vertical up
            count += 1
        if check_word(row, col, 1, 1):  # Diagonal down-right
            count += 1
        if check_word(row, col, 1, -1):  # Diagonal down-left
            count += 1
        if check_word(row, col, -1, 1):  # Diagonal up-right
            count += 1
        if check_word(row, col, -1, -1):  # Diagonal up-left
            count += 1

# Print the total count of occurrences
print(count)
