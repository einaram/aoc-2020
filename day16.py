import math
from operator import itemgetter


def read_indata(datatype='test'):
    return open(f"input/16.{datatype}.txt")


def parse_rules_part(data):
    rules = {}
    for row in data:
        row = row.strip()
        if not row:
            break
        key, values = row.split(':')
        values = [([int(y) for y in x.split('-')]) for x in values.split('or')]
        rules[key.strip()] = values
    return rules


def parse_other_tickets_part(data):
    return [[int(y) for y in row.split(',')]for row in data]


def field_invalid(value, rules):
    for r_min, r_max in rules:
        if r_min <= value <= r_max:
            break
    else:
        return True


def parse_data(data):

    rules = parse_rules_part(data)

    next(data)  # "your ticket:""
    my_ticket = [int(x) for x in next(data).split(',')]

    next(data)  # blank
    next(data)  # "nearby tickets:"
    other_tickets = parse_other_tickets_part(data)

    return rules, my_ticket, other_tickets


def find_valid(rules, other_tickets):
    invalid_counter = 0
    valid_tickets = []
    rules_ranges = [item for sublist in rules.values() for item in sublist]
    for ticket in other_tickets:
        invalid_values = [
            field for field in ticket if field_invalid(field, rules_ranges)]
        if not invalid_values:
            valid_tickets.append(ticket)
        invalid_counter += sum(invalid_values)
    print(invalid_counter)
    return invalid_counter, valid_tickets


rules, my_ticket, other_tickets = parse_data(read_indata('input'))
assert find_valid(rules, other_tickets)[0] == 21978


def get_valid(rules, value):
    valid = []
    for key, vranges in rules.items():
        for r_min, r_max in vranges:
            if r_min <= value <= r_max:
                valid.append(key)
    return set(valid)


rules, my_ticket, other_tickets = parse_data(read_indata('input'))
_, valid_tickets = find_valid(rules, other_tickets)

valid_per_column = [[] for x in range(len(valid_tickets[0]))]


for ticket in valid_tickets:
    for v, value in enumerate(ticket):
        valid_fields = get_valid(rules, value)
        valid_per_column[v].append(valid_fields)


valid_per_column = [set.intersection(*col) for col in valid_per_column]
sorted_valid_per_column = sorted(valid_per_column, key=len, reverse=True)

field_positions = {}
for c, col in enumerate(sorted_valid_per_column):
    field = col.difference(*sorted_valid_per_column[c+1:])
    field_positions[field.pop()] = valid_per_column.index(col)


dep_field = [v for k, v in field_positions.items() if "departure" in k]


deps = itemgetter(*dep_field)(my_ticket)
assert math.prod(deps) == 1053686852011
