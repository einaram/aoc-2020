import re


def read_indata(datatype='test1'):
    with open(f"input/19.{datatype}.txt") as infile:
        rules,data = infile.read().split("\n\n")

        rules_dict = {}
        for rule in rules.split('\n'):
            k,v = rule.split(':')
            rules_dict[k]=[[y for y in x.split()] for x in  v.split('|')]

        data = [x for x in data.split('\n')]
        return data, rules_dict

data, rules = read_indata()

def check_part(char, rule, rules):
    pass

def apply_rule(msg, rule, rules):
    for char in msg:
        if type(rule) == list and len(rule ) > 1:
            return all([apply_rule(char, rules[r], rules) for r in rule])
        elif char == rule[0][0].strip('"'): #char and rule ar both a or b
            return True
        elif rule.isdigit():
            return apply_rule(char, rules[rule], rules)
        else:
            pass

    pass

def apply_rules(msg, rules):
    return (all([apply_rule(msg, r, rules) for r in rules['0']]))


#     pass
# def check_rules(msg, rules):


#     pass

for msg in data:
    apply_rules(msg, rules)