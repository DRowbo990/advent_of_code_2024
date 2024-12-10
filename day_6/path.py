import sys

DIRECTION = "^"  # Initial direction

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 path.py <inputfile>")
    sys.exit(1)

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Open the file in read mode and read it into a 2D array of characters
with open(input_file, "r") as file:
    array_2d = [list(line.strip()) for line in file]

# Define the characters to search for
chars_to_find = ["^", ">", "v", "<"]

guards = True  # Flag to control the main loop

# Initialize a set to keep track of visited positions
visited_positions = set()


# Function to find the coordinates of a given character in the 2D array
def find_char(direction):
    """
    Finds the coordinates of the first occurrence of a specified character in a 2D array.

    Args:
        direction (str): The character to search for in the 2D array.

    Returns:
        tuple: A tuple (x, y) representing the coordinates of the character in the 2D array.
               If the character is not found, returns (None, None).
    """
    for x in range(len(array_2d)):
        for y in range(len(array_2d[x])):
            if array_2d[x][y] == direction:
                return x, y
    return None, None


# Function to move in the given direction from the current position
def move(x, y, direction):
    """
    Move a position in a 2D array based on the given direction.

    Parameters:
    x (int): The current x-coordinate (row index).
    y (int): The current y-coordinate (column index).
    direction (str): The direction to move in. Can be one of the following:
                     "^" for up, "v" for down, "<" for left, ">" for right.

    Returns:
    tuple: A tuple (new_x, new_y) representing the new coordinates after the move.
           If the move is out of bounds or hits a wall, returns (-1, -1).
    """
    if direction == "^":  # Move up
        if x - 1 < 0:  # Check for boundary
            return -1, -1
        elif array_2d[x - 1][y] == "#":  # Check for wall
            return x, y
        return x - 1, y
    elif direction == "v":  # Move down
        if x + 1 >= len(array_2d):  # Check for boundary
            return -1, -1
        elif array_2d[x + 1][y] == "#":  # Check for wall
            return x, y
        return x + 1, y
    elif direction == "<":  # Move left
        if y - 1 < 0:  # Check for boundary
            return -1, -1
        elif array_2d[x][y - 1] == "#":  # Check for wall
            return x, y
        return x, y - 1
    elif direction == ">":  # Move right
        if y + 1 >= len(array_2d[x]):  # Check for boundary
            return -1, -1
        elif array_2d[x][y + 1] == "#":  # Check for wall
            return x, y
        return x, y + 1
    return x, y


# Main loop to move the character until it can't move anymore
while guards:
    x, y = find_char(DIRECTION)  # Find the current position of the character
    if x is None or y is None:  # If character not found, exit loop
        guards = False
        break
    visited_positions.add((x, y))  # Add current position to visited positions
    x2, y2 = move(x, y, DIRECTION)  # Move to the next position
    if x == x2 and y == y2:  # Hit a wall or boundary
        DIRECTION = chars_to_find[
            (chars_to_find.index(DIRECTION) + 1) % 4
        ]  # Change direction
        array_2d[x][y] = DIRECTION  # Update the character in the array
    elif x2 == -1 and y2 == -1:  # If move is out of bounds, exit loop
        guards = False
        break
    else:
        array_2d[x][y] = "X"  # Mark the current position as visited
        array_2d[x2][y2] = DIRECTION  # Move the character to the new position

# print the 2D array
for row in array_2d:
    print("".join(row))

# Print the number of distinct positions visited
print("Number of distinct positions visited:", len(visited_positions))
