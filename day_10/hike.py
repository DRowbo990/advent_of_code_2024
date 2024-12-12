import sys  # Import the sys module to access command-line arguments

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print(
        "Usage: python3 hike.py <inputfile>"
    )  # Print usage message if incorrect arguments
    sys.exit(1)  # Exit the program with an error code

# Get the input file from the command line arguments
input_file = sys.argv[1]

# Read the input file and store each character in a 2D array
trails = []
with open(input_file, "r") as file:  # Open the input file for reading
    for line in file:  # Iterate over each line in the file
        trails.append(list(line.strip()))
        # Strip newline characters and convert to list of characters


def find_trail(trails, x, y):
    """
    Finds the number of reachable cells with a height of 9 starting from a given cell (x, y) in a grid of trails.

    Args:
        trails (list of list of str): A 2D grid representing the heights of the trails.
        x (int): The starting x-coordinate.
        y (int): The starting y-coordinate.

    Returns:
        int: The number of reachable cells with a height of 9.
    """
    queue = [(x, y)]  # Initialize a list with the starting cell
    visited = set()  # Create a set to keep track of visited cells
    visited.add((x, y))  # Mark the starting cell as visited
    reachable_nines = set()  # Create a set to store reachable cells with height 9

    while queue:  # Process cells in the queue until it's empty
        cx, cy = queue.pop(0)  # Dequeue the next cell (pop from the front)
        current_height = int(trails[cx][cy])  # Get the height of the current cell

        if current_height == 9:  # If the current cell has a height of 9
            reachable_nines.add((cx, cy))  # Add it to the set of reachable nines
            continue  # Continue to the next iteration

        # Check all four possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = (
                cx + dx,
                cy + dy,
            )  # Calculate the coordinates of the neighboring cell
            # Check if the neighboring cell is within bounds and not visited
            if (
                0 <= nx < len(trails)
                and 0 <= ny < len(trails[0])
                and (nx, ny) not in visited
            ):
                # Get the height of the neighboring cell
                next_height = int(trails[nx][ny])
                # If the neighboring cell height is one more than the current cell
                if next_height == current_height + 1:
                    queue.append((nx, ny))  # Add the neighboring cell to the queue
                    visited.add((nx, ny))  # Mark the neighboring cell as visited

    return len(reachable_nines)  # Return the number of reachable cells with height 9


# Find all trailheads and calculate their scores
total_score = 0  # Initialize the total score
for i, row in enumerate(trails):  # Iterate over each row in the trails grid
    for j, char in enumerate(row):  # Iterate over each character in the row
        if char == "0":  # If the character is '0', it is a trailhead
            total_score += find_trail(
                trails, i, j
            )  # Add the score of the trail starting from this trailhead

print(total_score)  # Print the total score
