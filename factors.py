#!/usr/bin/env python3

import sys


def factorize(number):
    # This function returns a tuple of two factors of the number
    # that are not necessarily prime.
    for i in range(2, number):
        if number % i == 0:
            return (i, number // i)
    return (1, number)


def main(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factorize(number)
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except ValueError:
        print("The file contains invalid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        main(sys.argv[1])
