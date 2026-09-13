#!/usr/bin/env python3

from calendar import day_abbr
from ctypes import sizeof
import re


def file_listing(filename="src/listing.txt"):
    pass

def main():
    result = file_listing()

    print(len(result))
    # Expected: 47

    for t in result:
        print(len(t))
    # Expected: all 6s, since each tuple has six elements

    for t in result:
        print(f"Items in result should be tuples and they are {type(t)}")
        print(f"First item in tuple (size) should be an int, is {type(t[0])}")
        print(f"Second item in tuple (month) should be a str, is {type(t[1])}")
        print(f"Third item in tuple (day) should be an int, is {type(t[2])}")
        print(f"Fourth item in tuple (hour) should be an int, is {type(t[3])}")
        print(f"Fifth item in tuple (minute) should be an int, is {type(t[4])}")
        print(f"Sixth item in tuple (filename) should be a str, is {type(t[5])}")


if __name__ == "__main__":
    main()
