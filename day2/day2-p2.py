import sys
import re
line_re = r"(\d+)\-(\d+)\s([a-zA-Z]):\s([a-zA-Z].+)"
matcher = re.compile(line_re)

with open('input.txt') as f:
    lines = f.readlines()
    valid_count = 0

    for line1 in lines:
        result = matcher.match(line1)
        first, second, letter, password = result.groups()
        first = int(first) - 1
        second = int(second) - 1
        l1 = password[first]
        l2 = password[second]

        if (l1 == letter or l2 == letter) and l1 != l2:
            valid_count += 1

    print(f"Valid Passwords: {valid_count}")