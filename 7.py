def read_rulesfile(datatype="input"):
    with open(f"input/7.{datatype}.txt") as infile:
        return infile.read().split("\n")

def parse_rules(raw_rules):
    rules_dict = {}
    for line in raw_rules:
        bag, rules = line.replace("bags", '').replace(
            "bag", '').split("contain")

        rules_dict[bag.strip()] = {r[2:].strip(): r[:2].strip() for r in rules.strip(".").split(",") if not "no other" in r}
    return rules_dict


def check_rule(rule, rules, lookup_bag, can_contain_cache=None):
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
            can_contain, can_contain_cache= check_rule(
                subrule, rules, lookup_bag, can_contain_cache)
            if can_contain:
                break

    # if can_contain:
        # can_contain_cache['']
    return can_contain, can_contain_cache


def check_rules(rules, lookup_bag):
    counter = 0
    for rule in rules:
        can_contain, can_contain_cache = check_rule(rule, rules, lookup_bag)
        if can_contain: 
            counter +=1
    print(counter)


raw_rules = read_rulesfile()
rules = parse_rules(raw_rules)

assert check_rules(rules, 'shiny gold') ==192
# assert 1