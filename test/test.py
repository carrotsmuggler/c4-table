import subprocess
import difflib
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "id", nargs="?", default=None, type=int, help="ID of the test to run"
)
args = parser.parse_args()

commands = []
# Open the file
with open("test_commands.txt", "r") as file:
    # Read each line
    for line in file:
        # Strip leading and trailing whitespace and split the line into a list of words
        command = line.strip().split()
        # Add the command to the list of commands
        commands.append(command)

# If an ID was provided, run only the test with that ID
if args.id:
    ids = [args.id]
else:
    # Otherwise, run all tests
    ids = range(1, len(commands) + 1)

for i in ids:
    command = commands[i - 1]
    output = subprocess.check_output(command).decode().strip()
    fname = f"test{i:02}.dat"
    # Load the expected output from a file
    with open(f"{fname}", "r") as file:
        expected_output = file.read().strip()
    # Assert that the output matches the expected output
    try:
        assert output == expected_output
        print(f"Passed test {i:02}")
    except AssertionError:
        diff = difflib.unified_diff(
            expected_output.splitlines(),
            output.splitlines(),
            fromfile="expected_output",
            tofile="output",
            lineterm="",
        )
        print("\n".join(diff))
        raise
