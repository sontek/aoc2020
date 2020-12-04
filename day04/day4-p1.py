import os
import argparse
import pytest
from support import timing

here = os.path.dirname(os.path.realpath(__file__))
default_file = os.path.join(here, "input.txt")

REQUIRED_FIELDS = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
}


def compute(lines):
    current_passport = {}
    count = 0

    for line in lines:
        data = line.split()
        for item in data:
            key, value = item.split(':')
            current_passport[key] = value

        if current_passport.keys() >= REQUIRED_FIELDS:
            count += 1

        current_passport = {}

    return count


TEST_INPUTS1 = '''\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUTS1, 2),
    ),
)
def test_compute(input_s, expected):
    result = compute(input_s.split("\n\n"))
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
        lines = f.read().split("\n\n")
        print(compute(lines))

    return 0


if __name__ == '__main__':
    exit(main())
