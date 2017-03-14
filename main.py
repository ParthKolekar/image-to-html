#!/usr/bin/env python3

from PIL import Image
import sys
import os
from itertools import groupby


def main():
    if len(sys.argv) != 2:
        print("Usage: main.py file", file=sys.stderr)
        sys.exit(-1)
    if not os.access(sys.argv[1], os.R_OK):
        print("Usage: main.py file", file=sys.stderr)
        print("Invalid File", file=sys.stderr)
        sys.exit(-1)

    pic = Image.open(sys.argv[1])
    data = pic.load()

    darray = []

    for i in range(pic.height):
        darray.append([data[j, i] for j in range(pic.width)])

    print("<table style=\"border-spacing:0; border-collapse: collapse;\">")
    for i in range(pic.height):
        print("<tr>")
        for element, list_of_elements in groupby(darray[i]):
            x = tuple(list(element) + [len(list(list_of_elements))])
            print("<td style=\"background-color:rgba(%d, %d, %d); margin:0; padding: 0; height: 1px; width: 1px;\" colspan=\"%d\"></td>" % x)
        print("</tr>")

    print("</table>")


if __name__ == '__main__':
    main()
