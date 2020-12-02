import os
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(lines):
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                i1 = int(lines[i])
                i2 = int(lines[j])
                i3 = int(lines[k])

                if i1 + i2 + i3 == 2020:
                    return i1 * i2 * i3


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("1721 979 366 299 675 1456", 241861950),
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
