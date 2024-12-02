import sys  # Import the sys module to access command-line arguments


def is_safe(columns):
    """
    Determines if the given list of columns is "safe".

    A list of columns is considered safe if:
    1. The difference between consecutive columns is not zero and does not exceed 3.
    2. The sequence of columns is either strictly increasing or strictly decreasing.

    Parameters:
    columns (list of int): A list of integers representing the columns.

    Returns:
    bool: True if the columns are safe, False otherwise.
    """
    safe = True  # Initialize the safe flag to True
    increasing = (
        None  # None means we haven't determined if it's increasing or decreasing yet
    )

    for i in range(
        1, len(columns)
    ):  # Iterate through the columns starting from the second element
        diff = (
            columns[i] - columns[i - 1]
        )  # Calculate the difference between consecutive columns
        if diff == 0 or abs(diff) > 3:  # Check if the difference is zero or exceeds 3
            safe = False  # Set safe to False if the condition is met
            break  # Exit the loop early
        if increasing is None:  # Determine if the sequence is increasing or decreasing
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False
        else:
            if (increasing and diff < 0) or (
                not increasing and diff > 0
            ):  # Check for sequence consistency
                safe = False  # Set safe to False if the sequence is inconsistent
                break  # Exit the loop early

    return safe  # Return the safe flag


def is_safe_with_dampener(columns):
    """
    Determines if the given columns configuration is safe, either directly or by removing one column.

    This function first checks if the given columns configuration is safe by calling the `is_safe` function.
    If the configuration is not safe, it then iterates through each column, removes it, and checks if the
    resulting configuration is safe. If any of these modified configurations are safe, the function returns True.

    Args:
        columns (list): A list representing the columns configuration.

    Returns:
        bool: True if the columns configuration is safe or can be made safe by removing one column, False otherwise.
    """
    if is_safe(columns):  # Check if the original columns configuration is safe
        return True  # Return True if it is safe

    for i in range(len(columns)):  # Iterate through each column
        new_columns = columns[:i] + columns[i + 1 :]  # Remove the current column
        if is_safe(new_columns):  # Check if the modified configuration is safe
            return True  # Return True if any modified configuration is safe

    return False  # Return False if no configuration is safe


tot = 0  # Initialize the total count of safe configurations to 0

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 levels.py <inputfile>")  # Print usage message
    sys.exit(1)  # Exit the program with an error code

# Get the input file from the command line arguments
input_file = sys.argv[1]

with open(input_file) as file:  # Open the input file for reading
    for line in file:  # Iterate through each line in the file
        columns = list(map(int, line.split()))  # Convert the line to a list of integers
        if is_safe_with_dampener(
            columns
        ):  # Check if the columns configuration is safe with dampener
            tot += 1  # Increment the total count if it is safe

print(tot)  # Print the total count of safe configurations
