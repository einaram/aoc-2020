# %%
import numpy as np
import random
import re


def read_indata(datatype='test'):
    with open(f"input/20.{datatype}.txt") as infile:
        images = {}
        sides_dict = {}
        for image in infile.read().replace('#', '1').replace('.', '0').split("\n\n"):
            img = [list(x) for x in image[11:].split('\n')]
            images[image[5:9]] = np.array(img)
            sides_dict[image[5:9]] = get_sides(images[image[5:9]])

        return images, sides_dict


SIDE_SLICE = {
    'left': np.s_[:, 0],
    'right': np.s_[:, -1],
    'top': np.s_[0, :],
    'bottom': np.s_[-1, :]
}
OPPOSITES = {'left': 'right',
             'right': 'left',
             'top': 'bottom',
             'bottom': 'top'}


def get_side(side, arr):
    return tuple(arr[SIDE_SLICE[side]])


def get_sides(arr):
    return frozenset([get_side(side, arr) for side in SIDE_SLICE])


def rotate_match(images, match_id, curr_id, side):
    to_match = get_side(side, images[curr_id])
    adj_side = OPPOSITES[side]

    for action in [\
            np.rot90, np.rot90, np.rot90, np.rot90, \
            np.flip, np.rot90, np.rot90, np.rot90, np.rot90, np.flip,\
            np.fliplr, np.rot90, np.rot90, np.rot90, np.rot90,np.fliplr, \
            np.flipud, np.rot90, np.rot90, np.rot90, np.rot90]:        # 4 rot90 to "reset".
        matched_side = get_side(adj_side, images[match_id])
        if matched_side == to_match:
            return images
        else:
            if match_id in grid.values():
                print("rotating fixed part")

            images[match_id] = action(images[match_id])
    else:
        print("NO MATCH")
        return images


def find_surrounding(images, sides_dict, grid, curr_id):
    x, y = [k for k, v in grid.items() if v == curr_id][0]
    # top:
    side = 'top'
    t = find_side_match(curr_id, get_side(side, images[curr_id]), sides_dict)
    if t:
        images = rotate_match(images, t[0], curr_id, side)
        grid[(x, y-1)] = t[0]
    # right
    r = find_side_match(curr_id,  get_side(
        'right', images[curr_id]), sides_dict)
    if r:
        images = rotate_match(images, r[0], curr_id, 'right')
        grid[(x+1, y)] = r[0]

    d = find_side_match(curr_id,  get_side(
        'bottom', images[curr_id]), sides_dict)
    if d:
        images = rotate_match(images, d[0], curr_id, 'bottom')
        grid[(x, y+1)] = d[0]

    l = find_side_match(curr_id,  get_side(
        'left', images[curr_id]), sides_dict)
    if l:
        images = rotate_match(images, l[0], curr_id, 'left')
        grid[(x-1, y)] = l[0]
    return grid, images


def find_side_match(search_id, side, sides_dict):
    match = [k for k, v in sides_dict.items(
    ) if k != search_id and (side in v or side[::-1] in v)]
    if len(match) > 1:
        raise "WTF"

    return match


def find_match(search_id, sides_dict, used):
    return [k for k, v in sides_dict.items() if k not in used and k != search_id and v.intersection(sides_dict[search_id])]


images, sides = read_indata('input')
used = []
parts = list(images.keys())
grid = {}
grid[(0, 0)] = parts[0]
while len(grid) < len(sides):
    # lazy but slow way to check all
    partid = random.choice(list(grid.values()))
    grid, images = find_surrounding(images, sides, grid,  partid)

# %%


def zero_index_grid(grid):
    def rename(key, dx, dy):
        x = key[0]+dx
        y = key[1]+dy
        return (x, y)
    # make grid zero-index:
    x_offs = abs(min([x[0] for x in grid]))
    y_offs = abs(min([x[1] for x in grid]))
    return {rename(k, x_offs, y_offs): v for k, v in grid.items()}


grid = zero_index_grid(grid)
# %%

def plot_part1(grid):
    import matplotlib.pyplot as plt
    plt.scatter(*zip(*grid.keys()))
    for i, kv in enumerate(grid.items()):
        k, v = kv
        plt.annotate(v, (k[0], k[1]))
    plt.show()
# plot_part1(grid)

# %%


def build_matrix(grid, images, cut=False):
    parts_size = max([x[0] for x in grid])+1
    sub_size = len(images[list(images)[0]][0])
    if cut:
        sub_size = sub_size-2
    size = parts_size*sub_size
    image = np.zeros((size, size), dtype=int)
    ids = np.zeros((parts_size, parts_size))

    for x, y in grid:
        dx = np.s_[x*sub_size: (1+x)*sub_size]
        dy = np.s_[y*sub_size:(1+y)*sub_size]
        if cut:
            image[dy, dx] = images[grid[(x, y)]][1:-1, 1:-1]

        else:
            image[dy, dx] = images[grid[(x, y)]]
        ids[(x, y)] = grid[(x, y)]

    return image, ids


img, ids = build_matrix(grid, images)

p1 = ids[0,0]*ids[-1,0]*ids[0,-1]*ids[-1,-1] # read corners: 3607*1697*1399*2731 -> 23386616781851
print('p1', p1)
# print(ids)

# %%
img, ids = build_matrix(grid, images, cut=True)


def find_monster(img):
    monster_parts = 15
    monster_re = re.compile(r""".{18}1.+\n
                            .*1.{4}11.{4}11.{4}111.*\n
                            .*1..1..1..1..1..1""", re.X)
    for action in [\
            np.rot90, np.rot90, np.rot90, np.rot90, \
            np.flip, np.rot90, np.rot90, np.rot90, np.rot90, np.flip,\
            np.fliplr, np.rot90, np.rot90, np.rot90, np.rot90,np.fliplr, \
            np.flipud, np.rot90, np.rot90, np.rot90, np.rot90]:
        img = action(img)
        img_str = np.array_str(img).replace(' ', '').replace('[', '').replace(']', '')

        if monster_re.findall(img_str):
            return len(monster_re.findall(img_str))*monster_parts 
    else:
        print('No monsters')

monster_parts = find_monster(img)

roughness = np.sum(img) - monster_parts
roughness
# %%
