import os
import re
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
    ecl_vals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hcl_matcher = re.compile(r'^#[0-9a-f]{6}$')
    pid_matcher = re.compile(r'^[0-9]{9}$')

    def hgt(val):
        if val.endswith('cm'):
            return 150 <= int(val[:-2]) <= 193
        elif val.endswith('in'):
            return 59 <= int(val[:-2]) <= 76

    validator = {
        "byr": lambda val: 1920 <= int(val) <= 2002,
        "iyr": lambda val: 2010 <= int(val) <= 2020,
        "eyr": lambda val: 2020 <= int(val) <= 2030,
        "hgt": hgt,
        "hcl": lambda val: bool(hcl_matcher.match(val)),
        "ecl": lambda val: val in ecl_vals,
        "pid": lambda val: bool(pid_matcher.match(val)),
        "cid": lambda val: True
    }

    for line in lines:
        data = line.split()

        for item in data:
            key, value = item.split(':')

            if validator[key](value):
                current_passport[key] = value

        if current_passport.keys() >= REQUIRED_FIELDS:
            count += 1

        current_passport = {}

    return count


TEST_INPUTS1 = '''\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:218 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (TEST_INPUTS1, 4),
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
