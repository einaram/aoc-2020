# %%
import numpy as np
import random
import re
from scipy import ndimage

def read_indata(datatype='input'):
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


def tile_orientations(tile):
    for r in range(4):
        a = np.rot90(tile, r)
        yield a
        yield np.fliplr(a)
        yield np.flipud(a)
        yield np.flipud(np.fliplr(a))

def rotate_match(images, match_id, curr_id, side):
    to_match = get_side(side, images[curr_id])
    adj_side = OPPOSITES[side]

    matched_side = get_side(adj_side, images[match_id])
    if matched_side == to_match:
        return images
    for tile in tile_orientations(images[match_id]):
        matched_side = get_side(adj_side, tile)
        if match_id in grid.values():
            print("rotating fixed part")
        if matched_side == to_match:
            images[match_id] = tile
            return images

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


img_uncut, ids = build_matrix(grid, images)

p1 = ids[0,0]*ids[-1,0]*ids[0,-1]*ids[-1,-1] # read corners: 3607*1697*1399*2731 -> 23386616781851
print('p1', p1)
# assert int(p1) ==  20899048083289
assert int(p1) ==  23386616781851

# %%
img, ids = build_matrix(grid, images, cut=True)


def find_monster(img):


    sea_monster = np.array(\
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
    def count_monsters(image, monster=sea_monster):
        return (ndimage.correlate(image, monster, mode='constant') == monster.sum()).sum()


    monster_re1=r"{s1}..................1.{e}\n"
    monster_re2=r"{s0}1....11....11....111{e}\n"
    monster_re3=r"{s0}.1..1..1..1..1..1...{e}\n"
    monster_re = monster_re1 + monster_re2 +monster_re3
    monster_re_c = re.compile(monster_re.format(s0='.*', s1='.*', e='.*'), re.X)
    monster_parts = 15
    for img in tile_orientations(img):
        m=count_monsters(img)
        img_str = str(img.tolist()).replace(' ', '').replace('],', '\n').replace('[', '').replace(']', '').replace(',','') 
        # Scipy from reddit + custom regex:      
        if m and False:
            z = 0
            for x in range(len(img[0])-20):
                s0 = f'.{{{x}}}'
                s1 = f'(?:^|\n).{{{x}}}'
                e= f".{{{len(img[0])-20-x}}}"
                dz=re.findall(monster_re.format(s0=s0, s1=s1, e=e),img_str)
                z += len(dz)
            
            print("reddit:",m,"regex:", z)
            print(re.compile(monster_re.format(s1=s1, s0=s0, e=e)))
            return m*monster_parts
        
        # Pure regex+loop
        if monsters := monster_re_c.findall(img_str):
            z = 0
            for x in range(len(img[0])-20):
                s0 = f'.{{{x}}}'
                s1 = f'(?:^|\n).{{{x}}}'
                e= f".{{{len(img[0])-20-x}}}"
                dz=re.findall(monster_re.format(s0=s0, s1=s1, e=e),img_str)
                z += len(dz)
            if z>0:
                print(z)
                return z*monster_parts

    else:
        print('No monsters')


monster_parts = find_monster(img)

roughness = np.sum(img) - monster_parts
print(roughness)
# assert int(roughness) == 273 # test
assert int(roughness) == 2376 # full
# %%
