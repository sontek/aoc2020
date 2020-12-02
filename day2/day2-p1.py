import sys
import re
line_re = r"(\d+)\-(\d+)\s([a-zA-Z]):\s([a-zA-Z].+)"
matcher = re.compile(line_re)

with open('input.txt') as f:
    lines = f.readlines()
    valid_count = 0

    for line1 in lines:
        result = matcher.match(line1)
        small, big, letter, password = result.groups()
        small = int(small)
        big = int(big)
        letter_count = password.count(letter)
        good = letter_count >= small and letter_count <= big
        if good:
            valid_count += 1

    print(f"Valid Passwords: {valid_count}")