def get_groupansw_fromfile(datatype="input"):
    with open(f"input/6.{datatype}.txt") as infile:
        return infile.read().split("\n\n")


def group_any_count(group_answers):
    #Testing list comp. vs filter vs replace.  Filter or replace wins IMO. 
    # Maybe split to two for readability
    # all_replace = [len(set(answ.replace("\n", ""))) for answ in group_answers]
    # all_lc = [len(set([char for char in answ if char.isalpha()])) for answ in group_answers]
    all_ = [len(set(filter(str.isalpha, answ))) for answ in group_answers]

    return sum(all_)


# B

def group_all_count(group):
    group_answers = [set(x) for x in group.split('\n')]
    return len(set.intersection(*group_answers))

if __name__ == "__main__":
    groups_answers = get_groupansw_fromfile()
    #A
    assert (group_any_count(groups_answers)) == 6625
    #B
    assert sum([group_all_count(group) for group in groups_answers]) == 3360
