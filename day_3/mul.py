import sys  # Import the sys module for command line arguments
import re  # Import the re module for regular expressions

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 mul.py <inputfile>")  # Print usage message
    sys.exit(1)  # Exit the program with an error code

# Get the input file from the command line arguments
input_file = sys.argv[1]

pattern = re.compile(r"mul\((\d+),(\d+)\)")  # Compile regex pattern for 'mul(x,y)'
do_pattern = re.compile(r"do\(\)")  # Compile regex pattern for 'do()'
dont_pattern = re.compile(r"don't\(\)")  # Compile regex pattern for 'don't()'
result = 0  # Initialize result to 0
enabled = True  # Initialize enabled flag to True

with open(input_file) as file:  # Open the input file
    for line in file:  # Iterate over each line in the file
        pos = 0  # Initialize position to 0
        while pos < len(line):  # Iterate over each character in the line
            if do_pattern.match(line, pos):  # Check for 'do()' pattern
                enabled = True  # Set enabled flag to True
                pos += len("do()")  # Move position past 'do()'
            elif dont_pattern.match(line, pos):  # Check for 'don't()' pattern
                enabled = False  # Set enabled flag to False
                pos += len("don't()")  # Move position past 'don't()'
            elif enabled and (
                match := pattern.match(line, pos)
            ):  # Check for 'mul(x,y)' pattern if enabled
                x, y = map(int, match.groups())  # Extract x and y values
                result += x * y  # Add product of x and y to result
                pos += len(match.group(0))  # Move position past 'mul(x,y)'
            else:
                pos += 1  # Move to the next character

print(result)  # Print the final result
