# %%


with open("2.input.txt") as infile:
    data =infile.readlines()

testdata = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split("\n")

def validatorA(rule, letter, password):
    letter_count = password.count(letter)
    if letter_count >= rule[0] and letter_count <= rule[1]:
        return True
        

def validatorB(rule, letter, password):
    if sum([password[rule[0]-1] == letter,  password[rule[1]-1] == letter]) == 1:
        return True

def runner(data, validator= validatorA):
    valid_count = 0
    for row in data:
        row = row.split(" ")
        allowed_range = [int(x) for x in row[0].split("-")]
        letter = row[1].strip(":")
        password = row[2]
        if validator(allowed_range, letter, password):
            valid_count += 1
    return valid_count


# A
assert runner(testdata)== 2
print("A:", runner(data))


# %%
assert runner(testdata, validatorB) == 1
print("B:", runner(data, validatorB))

# %%
# A: 643
# B: 388
