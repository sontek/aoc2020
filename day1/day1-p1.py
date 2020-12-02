import sys

with open('input.txt') as f:
    lines = f.readlines()
    for line1 in lines:
        for line2 in lines[::1]:
            i1 = int(line1)
            i2 = int(line2)
            if i1 + i2 == 2020:
                print(f"Answer is: {i1 * i2}")
                sys.exit()