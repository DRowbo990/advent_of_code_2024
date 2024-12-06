import sys
from collections import defaultdict, deque

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 xmas.py <inputfile>")
    sys.exit(1)

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Read the input file
with open(input_file, "r") as file:
    lines = [line.strip() for line in file if line.strip()]

# Separate the ordering rules and updates
rules = []
updates = []
reading_rules = True

for line in lines:
    if "|" in line:
        rules.append(line)
    else:
        updates.append(line)

# Build the graph from the rules
graph = defaultdict(list)
in_degree = defaultdict(int)

for rule in rules:
    x, y = rule.split("|")
    x, y = int(x), int(y)
    graph[x].append(y)
    in_degree[y] += 1
    if x not in in_degree:
        in_degree[x] = 0


# Function to check if an update is in the correct order
def is_correct_order(update):
    update_list = list(map(int, update.split(",")))
    position = {page: i for i, page in enumerate(update_list)}

    for x in update_list:
        for y in graph[x]:
            if y in position and position[x] > position[y]:
                return False
    return True


# Find the middle page number of a list
def find_middle(update_list):
    n = len(update_list)
    return update_list[n // 2]


# Process each update and check if it is in the correct order
correct_updates = []
for update in updates:
    if is_correct_order(update):
        correct_updates.append(list(map(int, update.split(","))))

# Find the middle page numbers of the correctly-ordered updates
middle_page_numbers = [find_middle(update) for update in correct_updates]

# Sum the middle page numbers
result = sum(middle_page_numbers)

# Print the result
print(result)
