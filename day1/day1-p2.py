import sys

with open('input.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                i1 = int(lines[i])
                i2 = int(lines[j])
                i3 = int(lines[k])

                if i1 + i2 + i3 == 2020:
                    print(f"Answer is: {i1 * i2 * i3}")
                    sys.exit()