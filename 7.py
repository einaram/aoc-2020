


def read_rulesfile(datatype="input"):
    with open(f"input/7.{datatype}.txt") as infile:
        return infile.read().split("\n")

def parse_rules(raw_rules):
    rules_dict = {}
    for line in raw_rules:
        bag, rules = line.replace("bags", '').replace(
            "bag", '').split("contain")
        rules_dict[bag.strip()] = {r[2:].strip(): int(r[:2].strip()) for r in rules.strip(".").split(",") if not "no other" in r}
    return rules_dict


def check_rule(rule, rules, lookup_bag, can_contain_cache=None, count = 0):
    can_contain = False
    if can_contain_cache == None:
        can_contain_cache = {}
    if can_contain_cache.get(lookup_bag) == True:
        #Bag is already checked and can contain lookup_bag
        can_contain= True
    elif can_contain_cache.get(lookup_bag) == False:
            #Bag is already checked and can NOT contain lookup_bag
        can_contain = False
    elif lookup_bag in rules[rule]:
        can_contain_cache[rule] = True
        can_contain = True
    else:
        for subrule in rules[rule]:
            can_contain, can_contain_cache, count= check_rule(
                subrule, rules, lookup_bag, can_contain_cache)
            if can_contain:
                break


    count = count + sum(rules[rule].values())

    return can_contain, can_contain_cache, count


def check_rules_for_bag(rules, lookup_bag):
    # counter = 0
    # for rule in rules:
    #     can_contain, can_contain_cache, count = check_rule(rule, rules, lookup_bag)
    #     if can_contain: 
    #         counter +=1
    counter = sum([1 for rule in rules if  check_rule(rule, rules, lookup_bag)[0]])
    print(counter)
    return counter


def part1():
    raw_rules = read_rulesfile()
    rules = parse_rules(raw_rules)
    # Part 1
    assert check_rules_for_bag(rules, 'shiny gold') == 192
# part1()

# Part 2

def check_bags_required(rules, lookup_bag):
    count = 0
    required_bags = rules[lookup_bag]
    if not required_bags:
        return 0
    for bag,bc in required_bags.items():
        count += bc
        count += bc*check_bags_required(rules, bag)
    return count


raw_rules = read_rulesfile()
rules = parse_rules(raw_rules)
count = check_bags_required(rules, 'shiny gold' )
assert count == 12128



