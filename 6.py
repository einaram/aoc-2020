def get_groupansw_fromfile(datatype="input"):
    with open(f"input/6.{datatype}.txt") as infile:
        answ_batch = [row.replace("\n", " ").replace(" ",'')
                           for row in infile.read().split("\n\n")]
    return [answ for answ in answ_batch]


#A
all_ = [len(set(answ)) for answ in get_groupansw_fromfile()  ]
sum_answ= sum(all_)
assert sum_answ == 6625

#B
for a in get_groupansw_fromfile('test'):
    pass    

# != 1509