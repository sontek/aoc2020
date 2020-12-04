import os
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute(lines):
    count = 0

    current_column = 3

    for row_index, line in enumerate(lines):
        if row_index != 0:
            tree = line[current_column]

            if tree == "#":
                count += 1

            current_column += 3
            current_column %= len(lines[0])

    return count


TEST_INPUTS = '''\
..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUTS, 7),
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
        print(compute(f.read().splitlines()))

    return 0


if __name__ == '__main__':
    exit(main())
