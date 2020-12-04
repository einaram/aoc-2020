# %%

from functools import partial

def readfile(datatype):
    with open(f"input/4.{datatype}.txt") as infile:
        passports_batch =infile.read().split("\n\n")
        passports_batch = [x.replace("\n", " ") for x in passports_batch]
        passports = []
        for passport in passports_batch:
            fields = {x.split(":")[0]: x.split(":")[1]
                      for x in passport.split(" ")}
            passports.append(fields)

    return passports



required_fields = set(["ecl", "pid", "eyr", "hcl",
                       "byr", "iyr", "hgt"])
optional_fields =set(["cid"])

# A
def validate_batch(required_fields, passport_batch):
    return sum([1 for x in passport_batch if required_fields.issubset(set(x)) ])
    
#B

# def validate_fields(passport):
#     if not required_fields.issubset(set(passport)):
#         return False
    

#     # def validate_year(year, ymin, ymax):
#     #     try:
#     #         year= int(year)
#     #         if year >= ymin and year <= ymax:
#     #             return True

#     # validators = {
#     #     'byr': partial(validate_year(1920, 2002))
#     #     }
#     # a = 12


# validate_fields(passport_batch[0])
    # iyr(Issue Year) - four digits
    # at least 2010 and at most 2020.
    # eyr(Expiration Year) - four digits
    # at least 2020 and at most 2030.
    # hgt(Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
    # ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid(Passport ID) - a nine-digit number, including leading zeroes.
    # cid(Country ID) - ignored, missing or not.




# A
assert validate_batch(required_fields, readfile("test")) == 2
assert validate_batch(required_fields, readfile("data")) == 204
# print("A:", runner(data)) 


# B 
validate_batch(required_fields, readfile("test"))
validate_batch(required_fields, readfile("data"))

# %%
