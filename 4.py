# %%
import re
def split_passport_fields(passport):
    fields = {x.split(":")[0]: x.split(":")[1]
              for x in passport.split(" ")}
    return fields

def readfile(datatype):
    with open(f"input/4.{datatype}.txt") as infile:
        passports_batch = [row.replace("\n", " ")
                           for row in infile.read().split("\n\n")]

    return [split_passport_fields(passport) for passport in passports_batch]


required_fields = set(["ecl", "pid", "eyr", "hcl",
                       "byr", "iyr", "hgt"])

# A
def validate_batchA(required_fields, passport_batch):
    return sum([1 for x in passport_batch if required_fields.issubset(set(x))])

# B

def validate_year(ymin, ymax, year):
    if ymin <= int(year) <= ymax:
        return True

def validate_height(height_str):
    # hgt(Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    valid = False

    unit = height_str[-2:].lower()
    value = int(height_str[:-2])  # wrong if no unit
    if unit == 'cm':
        if  150 <= value <= 193:
            valid = True

    elif unit == "in":
        if 59 <= value <= 76:
            valid = True
    return valid


def field_is_valid(field, value):
    valid = False
    validators = {
        'byr': lambda year: validate_year(1920, 2002, year),

        # iyr(Issue Year) - four digits at least 2010 and at most 2020.
        'iyr': lambda year: validate_year(2010, 2020, year),

        # eyr(Expiration Year) - four digits  at least 2020 and at most 2030.
        'eyr': lambda year: validate_year(2020, 2030, year),

        'hgt': validate_height,

        # hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
        'hcl': lambda haircolor: re.match("#[0-9a-fA-F]{6}", haircolor),

        # ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        'ecl': lambda x: 1 if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else 0,

        # pid(Passport ID) - a nine-digit number, including leading zeroes.
        'pid': lambda pid: re.match("^[0-9]{9}$", pid),

        # cid(Country ID) - ignored, missing or not.
        'cid': lambda x: True
    }

    is_valid = validators.get(field)(value)
    return is_valid


def validate_passport(required_fields, passport):
    valid = True
    if required_fields.issubset(set(passport)):
        for field, value in passport.items():
            if not field_is_valid(field, value):
                valid = False
    else:
        valid = False
    return valid

def validate_batchB(required_fields, passport_batch):
    valid_passports = [validate_passport(required_fields, passport) for passport in passport_batch]
    return sum(valid_passports)

assert validate_batchB(required_fields, readfile("test_valid")) == 4
assert validate_batchB(required_fields, readfile("test_invalid")) == 0

assert validate_batchB(required_fields, readfile("data")) == 179

# A
assert validate_batchA(required_fields, readfile("test")) == 2
assert validate_batchA(required_fields, readfile("data")) == 204

# %%
