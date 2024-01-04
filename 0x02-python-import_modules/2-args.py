#!/usr/bin/python3
import sys

def print_argvs(args):
    """Prints the number and list of arguments.

    Args:
        args: A list of arguments.
    """

    number_of_args = len(args)
    if number_of_args == 0:
        print("0 arguments.")
    elif number_of_args == 1:
        print(f"1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{number_of_args} arguments:")
        for i in range(number_of_args):
            print(f"{i + 1}: {args[i]}")

if __name__ == "__main__":
    print_argvs(sys.argv[1:])
