def read_rulesfile(datatype="input"):
    with open(f"input/7.{datatype}.txt") as infile:
        return infile.read().split("\n")


def parse_rules(raw_rules):
    rules_dict = {}
    for line in raw_rules:
        bag, rules = line.replace("bags", '').replace(
            "bag", '').strip(".").split("contain")

        rules_dict[bag.strip()] = {r[2:].strip(): int(
            r[:2].strip()) for r in rules.split(",") if not "no other" in r}
    return rules_dict


def check_rule(rule, rules, lookup_bag):
    can_contain = False
    if lookup_bag in rules[rule]:
        can_contain = True
    else:
        for subrule in rules[rule]:
            can_contain = check_rule(
                subrule, rules, lookup_bag)
            if can_contain:
                break

    return can_contain


def check_rules_for_bag(rules, lookup_bag):
    counter = sum([1 for rule in rules if check_rule(rule, rules, lookup_bag)])
    return counter


# Part 1
def part1():
    raw_rules = read_rulesfile()
    rules = parse_rules(raw_rules)
    assert check_rules_for_bag(rules, 'shiny gold') == 192


part1()

# Part 2


def check_bags_required(rules, lookup_bag):
    count = 0
    required_bags = rules[lookup_bag]
    if not required_bags:
        return 0
    for bag, bagcount in required_bags.items():
        count += bagcount + bagcount*check_bags_required(rules, bag)
    return count


raw_rules = read_rulesfile()
rules = parse_rules(raw_rules)
count = check_bags_required(rules, 'shiny gold')
assert count == 12128
