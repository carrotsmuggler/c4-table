import subprocess
import concurrent.futures


# %% Run individual test
def run_command(command, i):
    fname = f"test{i:02}.dat"
    # Append the redirection to the command
    command += [">", fname]
    # Run the command in a shell
    subprocess.run(" ".join(command), shell=True)
    print(f"Generated {fname}")


# %% Read the commands
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

# %% Run all tests
# Run each command
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i, command in enumerate(commands, start=1):
        executor.submit(run_command, command, i)
