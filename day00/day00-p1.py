import os
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")

def compute(lines):
    # TODO: implement solution here!
    return 0


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("1 2 3 4", 0),
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
