# %%
from scipy.sparse import dok_matrix
import re
import numpy as np
import random


def read_indata(datatype='test'):
    with open(f"input/20.{datatype}.txt") as infile:
        images = {}
        sides_dict = {}
        for image in infile.read().split("\n\n"):
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
OPPOSITES = {'left':'right',
            'right': 'left',
            'top': 'bottom',
            'bottom': 'top'}


def get_side(side, arr):
    return tuple(arr[SIDE_SLICE[side]])


def get_sides(arr):
    return frozenset([get_side(side, arr) for side in SIDE_SLICE])

def rotate(images, matched,curr_id, side):
    to_match = get_side(side,images[curr_id])
    adj_side = OPPOSITES[side]

    for action in [np.rot90,np.rot90, np.rot90, np.rot90, np.flip, np.rot90,np.rot90, np.rot90, np.rot90, np.fliplr, np.rot90,np.rot90, np.rot90, np.rot90]:
        # 4 rot90 to "reset". np.array is a dummy
        matched_side = get_side(adj_side, images[matched] )
        if matched_side == to_match:
            return images
        else:
            images[matched] = action(images[matched])
    else:
        print("NO MATCH")
        return images


def find_surrounding(images, sides_dict, grid, curr_id):
    # curr_id = grid[coord]
    coord = [k for k, v in grid.items() if v == curr_id][0]
    # top:
    side = 'top'
    t= find_side_match(curr_id, get_side(side, images[curr_id]), sides_dict)
    if t:
        images = rotate(images, t[0],curr_id, side )
        grid[(coord[0], coord[1]+1)] = t[0]


    r  = find_side_match(curr_id,  get_side(
        'right', images[curr_id]), sides_dict)
    if r:
        images = rotate(images, r[0],curr_id, 'right' )
        grid[(coord[0]+1, coord[1])] = r[0]

    d  = find_side_match(curr_id,  get_side(
        'bottom', images[curr_id]), sides_dict)
    if d:
        images = rotate(images, d[0],curr_id, 'bottom' )
        grid[(coord[0], coord[1]-1)] = d[0]

    l  = find_side_match(curr_id,  get_side(
        'left', images[curr_id]), sides_dict)
    if l:
        images = rotate(images, l[0],curr_id, 'left' )
        grid[(coord[0]-1, coord[1])] = l[0]
    return grid, images


def find_side_match(search_id, side, sides_dict):
    # top(images[curr_id])
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
    partid = random.choice(list(grid.values()))
    grid, images = find_surrounding(images, sides, grid,  partid)
    print(partid)


# zero-index grid:
x_offs = abs(min([x[0] for x in grid]))
y_offs = abs(min([x[1] for x in grid]))


def rename(key, dx, dy):
    x = key[0]+dx
    y = key[1]+dy
    return (x, y)


# grid = {rename(k, x_offs, y_offs): v for k, v in grid.items()}
# %%
import matplotlib.pyplot as plt
plt.scatter(*zip(*grid.keys()))
for i, kv  in enumerate(grid.items()):
    k,v = kv
    plt.annotate(v, (k[0], k[1]))
plt.show()
# read corners from plot: 3607*1697*1399*2731 -> 23386616781851
# %%

x_max = abs(max([x[0] for x in grid]))
y_max = abs(max([x[1] for x in grid]))


out = dok_matrix((x_max, y_max), dtype=int)
out._update(grid)
out.todense()
out

# %%
