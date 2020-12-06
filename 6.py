def get_groupansw_fromfile(datatype="input"):
    with open(f"input/6.{datatype}.txt") as infile:
        answ_batch = [row.replace(" ",'')
                           for row in infile.read().split("\n\n")]
    return [answ for answ in answ_batch]

groups_answers = get_groupansw_fromfile()
#A
def group_any_count(group_answers):
    all_ = [len(set(answ.replace("\n", ""))) for answ in group_answers  ]
    return sum(all_)

assert (group_any_count(groups_answers)) == 6625


#B

def group_all_count(group):
    group_answers = [set(x) for x in group.split('\n')]
    return len(set.intersection(*group_answers))


assert sum([group_all_count(group) for group in groups_answers]) == 3360
# != 1509
