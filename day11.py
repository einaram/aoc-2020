import numpy as np
# nansum is ber
def read_rulesfile(datatype='test'):
    with open(f"input/11.{datatype}.in") as infile:
        data = infile.read().split("\n")
        data = [[float(x.replace("#", '1').replace("L", '0').replace(".", 'nan'))
                 for x in row] for row in data]
        return np.array(data)


def subset_slice(idx, xy_max):
    x, y = idx
    xmin = x-1 if x-1 > 0 else 0
    xmax = x+2 if x < xy_max[0] else xy_max[0]
    ymin = y-1 if y > 0 else 0
    ymax = y+2 if y < xy_max[1] else xy_max[1]

    return np.s_[xmin:xmax, ymin:ymax]


def rules1(idx, x, layout):
    s = subset_slice(idx, layout.shape)
    if x == 0 and np.nansum(layout[s]) == 0:
        x = 1
    elif x == 1 and np.nansum(layout[s]) > 4:
        x = 0
    return x


def check_directions(arr,idx):
    directions = {
        'u': (0,-1),
        'u_r': (1,-1),
        'r': (1,0),
        'd_r': (1,1),
        'd': (0,1),
        'd_l': (-1,1),
        'l': (-1,0),
        'u_l': (-1,-1)
    }
    count = 0
    dmax = arr.shape[:]
    for dir in directions.values():
        x,y = idx
        while True:
            x += dir[0]
            y += dir[1]
            if not (0 <= x < dmax[0]) or not (0 <= y < dmax[1]):
                break
            if arr[(x,y)] in (0, 1):
                count += arr[(x, y)]
                break
    return count


def rules2(idx, x, layout):
    seen = check_directions(layout, idx)
    if x == 0 and seen == 0:
        x = 1
    elif x == 1 and seen >= 5:
        x = 0
    return x


def apply_rules(rule_set, datafile='data'):
    layout = read_rulesfile(datafile)
    while True:
        new_l = np.copy(layout)
        for idx, x in np.ndenumerate(layout):
            new_l[idx] = rule_set(idx, x, layout)
        # new_l = [apply_rules(idx, x, layout, new_l)
        #      for idx, x in np.ndenumerate(layout)]
        # print(new_layout)
        # print("__________________________________________")
        if (np.nan_to_num(new_l) == np.nan_to_num(layout)).all():
            print(np.nansum(layout))
            break
        layout = new_l
    return np.nansum(layout)


# P1
assert apply_rules(rules1, 'data') == 2108.0

# P2
assert apply_rules(rules2, 'data') == 1897

# Tests
assert check_directions(read_rulesfile('none'), (3, 3)) == 0
assert check_directions(read_rulesfile('4,4-eigth'), (4, 3)) == 8
assert apply_rules(rules2, 'test') == 26
