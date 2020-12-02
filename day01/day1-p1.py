import os
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(lines):
    for line1 in lines:
        for line2 in lines[::1]:
            i1 = int(line1)
            i2 = int(line2)
            if i1 + i2 == 2020:
                return i1 * i2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("1721 979 366 299 675 1456", 514579),
    ),
)
def test_compute(input_s, expected):
    result = compute(input_s.split())
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
