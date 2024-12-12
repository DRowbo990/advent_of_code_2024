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


def find_trail_rating(trails, x, y):
    """
    Finds the number of distinct hiking trails starting from a given cell (x, y) in a grid of trails.

    Args:
        trails (list of list of str): A 2D grid representing the heights of the trails.
        x (int): The starting x-coordinate.
        y (int): The starting y-coordinate.

    Returns:
        int: The number of distinct hiking trails starting from the given cell.
    """

    def dfs(cx, cy, current_height):
        if current_height == 9:
            return 1
        total_trails = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(trails) and 0 <= ny < len(trails[0]):
                next_height = int(trails[nx][ny])
                if next_height == current_height + 1:
                    total_trails += dfs(nx, ny, next_height)
        return total_trails

    return dfs(x, y, 0)


# Find all trailheads and calculate their ratings
total_rating = 0  # Initialize the total rating
for i, row in enumerate(trails):  # Iterate over each row in the trails grid
    for j, char in enumerate(row):  # Iterate over each character in the row
        if char == "0":  # If the character is '0', it is a trailhead
            total_rating += find_trail_rating(
                trails, i, j
            )  # Add the rating of the trail starting from this trailhead

print(total_rating)  # Print the total rating
