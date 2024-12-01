import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 day1.py <inputfile>")
    sys.exit(1)

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Open the file in read mode
with open(input_file, "r") as file:
    # Initialize an empty list to store the first column values
    first_column = []
    second_column = []
    # Read the file line by line
    for line in file:
        # Split the line by whitespace (or any other delimiter)
        columns = line.split()

        # Append the first column value to the list
        if columns:  # Check if the line is not empty
            first_column.append(columns[0])
            second_column.append(columns[1])

first_column = [int(x) for x in first_column]
second_column = [int(x) for x in second_column]
# Sort the columns
first_column.sort()
second_column.sort()

output = [abs(first_column[i] - second_column[i]) for i in range(len(first_column))]
# print("Output:", output)
result = 0
for num in output:
    result = result + num
print(result)

# Part 2: Calculate the similarity score
similarity_score = 0
for num in first_column:
    count = second_column.count(num)
    similarity_score += num * count

# Print the similarity score
print(similarity_score)
