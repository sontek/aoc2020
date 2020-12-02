import os
import re
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")

line_re = r"(\d+)\-(\d+)\s([a-zA-Z]):\s([a-zA-Z].+)"
matcher = re.compile(line_re)


def compute(lines):
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

    return valid_count


TEST_INPUTS = '''\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUTS, 2),
    ),
)
def test_compute(input_s, expected):
    result = compute(input_s.splitlines())
    assert result == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    args = parser.parse_args()

    with open(args.f or default_file) as f, timing():
        print(compute(f.readlines()))

    return 0


if __name__ == '__main__':
    exit(main())