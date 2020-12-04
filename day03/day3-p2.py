import os
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")


def compute_step(lines, right_step, down_step):
    count = 0

    current_column = right_step

    for row_index in range(down_step, len(lines), down_step):
        line = lines[row_index]
        tree = line[current_column]

        if tree == "#":
            count += 1

        current_column += right_step

        # modulo the right step so that we can
        # repeat the pattern.  For example if
        # we have a line with 32 length, every
        # time we hit "32" we'll reset X back to
        # 0 to start over.
        current_column %= len(lines[0])

    return count


def compute(lines):
    steps = [
        {
            "down": 1,
            "right": 1,
        },
        {
            "down": 1,
            "right": 3,
        },
        {
            "down": 1,
            "right": 5,
        },
        {
            "down": 1,
            "right": 7,
        },
        {
            "down": 2,
            "right": 1,
        },
    ]

    result = 1
    for step in steps:
        if result != 0:
            result *= compute_step(lines, step['right'], step['down'])

    return result


TEST_INPUTS1 = '''\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''

TEST_INPUTS2 = '''\
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
        (TEST_INPUTS1, 336),
        (TEST_INPUTS2, 336),
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
        # don't use readlines because it leaves the
        # new lines in the output.  Which throws off
        # character count.
        # lines = f.readlines()
        lines = f.read().splitlines()
        print(compute(lines))

    return 0


if __name__ == '__main__':
    exit(main())
