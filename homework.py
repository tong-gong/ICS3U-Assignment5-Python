#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a Nested Loops program.


counter = 1


def main():
    # This is the function to run Nested Loops.

    userinput = input("Enter a number positive number: ")
    print("")

    # Process & output
    try:
        userinput = int(userinput)
        if userinput > 0:
            for counter in range(11):
                final = counter * userinput
                print("{} * {} = {}".format(userinput, counter, final))
        elif userinput < 0:
            print("It is not a positive integer.")
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()
