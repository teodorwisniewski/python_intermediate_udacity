# Import the sys library and replace the name variable with the appropriate argv index.
# Add a second argument representing the city and extend the print to include this argument.
# Try running python3 cli.py sam 'new york' and make sure you're getting the output: hello, sam from new york.
# Notice the single quotes in the cli argument to prevent new and york from being passed as two different arguments.

import sys

filename = sys.argv[0]
name = sys.argv[1].lower().title()
city = sys.argv[2].lower().title()
print(f"Running {filename}")
print(f"hello, {name} from {city}.")