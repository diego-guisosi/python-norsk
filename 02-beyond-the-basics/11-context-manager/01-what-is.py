# Context Manager is an object designed to be used in a with-statement, which ensures automatic management of resources
# The with statement basically executes code of the context manager before and after the code block
# With statement calls context_manager.enter() method to prepare the manager for use
# and after the body execution calss context_manager.exit() to clean it up

# files are context managers
with open("sample_file.txt", mode="rt") as file:
    # context-manager.enter()
    for line in file.readlines():
        print(line)
    # context-manager.exit()
