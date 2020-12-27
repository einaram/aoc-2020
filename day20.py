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

get_side= {
    'left': lambda arr: tuple(arr[:, 0]),
    'right': lambda arr: tuple(arr[:, -1]),
    'top': lambda arr: tuple(arr[0, :]),
    'bottom': lambda arr: tuple(arr[-1, :])
}



def get_sides(arr):
    return frozenset([v(arr) for v in get_side.values()])


def find_surrounding(images, sides_dict, grid, curr_id):
    # curr_id = grid[coord]
    coord = [k for k,v in grid.items() if v == curr_id ][0]
    # top:
    t = find_side_match(curr_id, top(images[curr_id]), sides_dict)
    if t:
        grid[(coord[0], coord[1]+1)] = t[0]

    r = find_side_match(curr_id, right(images[curr_id]), sides_dict)
    if r:
        grid[(coord[0]+1, coord[1])] = r[0]

    d = find_side_match(curr_id, bottom(images[curr_id]), sides_dict)
    if d:
        grid[(coord[0], coord[1]-1)] = d[0]

    l = find_side_match(curr_id, left(images[curr_id]), sides_dict)
    if l:
        grid[(coord[0]-1, coord[1])] = l[0]
    return grid


def find_side_match(search_id, side, sides_dict):
    top(images[curr_id])
    match = [k for k, v in sides_dict.items() if k != search_id and side in v or side[::-1] in v]

    return match


def find_match(search_id, sides_dict, used):
    return [k for k, v in sides_dict.items() if k not in used and k != search_id and v.intersection(sides_dict[search_id])]


images, sides = read_indata('test')
used = []
parts = list(images.keys())
grid = {}
grid[(0, 0)] = parts[0]
while len(grid) < len(sides):
    partid = random.choice(list(grid.values()))
    grid = find_surrounding(images, sides, grid,  partid)

grid

# zero-index grid:
x_offs = abs(min([x[0] for x in grid]))
y_offs = abs(min([x[1] for x in grid]))


def rename(key, dx,dy):
    x = key[0]+dx
    y = key[1]+dy
    return (x,y)
grid = {rename(k, x_offs, y_offs ):v for k,v in grid.items()}
grid

from scipy.sparse import dok_matrix

x_max = abs(max([x[0] for x in grid]))
y_max = abs(max([x[1] for x in grid]))


out = dok_matrix((x_max, y_max), dtype = int)
out._update(grid)
out.todense()
out