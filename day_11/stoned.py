import sys  # Import the sys module to access command-line arguments

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print(
        "Usage: python3 stoned.py <inputfile>"
    )  # Print usage message if incorrect arguments
    sys.exit(1)  # Exit the program with an error code

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Read the input file and store each character in a 2D array
stoned = []
with open(input_file, "r") as file:  # Open the input file for reading
    for line in file:  # Iterate over each line in the file
        elements = line.strip().split()  # Split the line into individual elements
        stoned.extend(elements)  # Append each element to the list

# Convert each element to an integer
stoned = [int(element) for element in stoned]


def process_stones(stones):
    for element in stones:
        if element == 0:
            yield 1
        elif len(str(element)) % 2 == 0:
            element_str = str(element)
            mid = len(element_str) // 2
            left = element_str[:mid].lstrip("0")
            right = element_str[mid:].lstrip("0")
            yield int(left) if left else 0
            yield int(right) if right else 0
        else:
            yield element * 2024


for _ in range(5):
    stoned = list(process_stones(stoned))

print(len(stoned))
