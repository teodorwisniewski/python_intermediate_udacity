# Replace the sys.argv in the provided code using the argparse module.
# Set a default paramater for the city argument.
# Read the man page for your CLI tool by running: python3 arg.py --help
# Try executing various inputs using python3 arg.py {name} {city}

import argparse

parser = argparse.ArgumentParser(description="Hello World!")
name = parser.add_argument("name", type=str)
city = parser.add_argument("--city", type=str, default="LA", help="Where is the person from?")

args = parser.parse_args()
name = args.name
city = args.city

print(f'hello, {name} from {city}')

# python3 arg.py --help