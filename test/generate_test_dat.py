import subprocess
import difflib

# Take out the commands
commands = []

# Open the file
with open("test_commands.txt", "r") as file:
    # Read each line
    for line in file:
        # Strip leading and trailing whitespace and split the line into a list of words
        command = line.strip().split()
        # Add the command to the list of commands
        commands.append(command)

# Run each command
# Run each command
for i, command in enumerate(commands, start=1):
    fname = f"test{i:02}.dat"
    # Append the redirection to the command
    command += [">", fname]
    # Run the command in a shell
    subprocess.run(" ".join(command), shell=True)
    print(f"Generated {fname}")
