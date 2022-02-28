#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on February 2022
# This is the Perimeter and Area for a rectangle with length & width inputted by user


def main():
    # this function calculates the area and perimeter
    # input
    Length = int(input("Enter the Length of the rectangle (mm): "))
    width = int(input("Enter the Width of the rectangle (mm): "))
    # process
    area = Length * width
    perimeter = 2 * (Length + width)
    # output
    print("")
    print("Area is {0} mm².".format(area))
    print("perimeter is {0} mm.".format(perimeter))
    print("\nFinished.")


if __name__ == "__main__":
    main()
