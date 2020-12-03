# %%


with open("3.input.txt") as infile:
    data =infile.readlines()

testdata = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")


test_valid = (2,7,3,4,2)


def run_single_route(mapdata, xstep=3, ystep=1):
    mapdata = [x.strip() for x in mapdata]
    trees = 0
    x_pos = 0
    map_width = len(mapdata[0])
    for y_row in mapdata[::ystep]:
        if y_row[x_pos%map_width] == "#":
            trees +=1
        x_pos += xstep
    return trees


# A
assert run_single_route(testdata)== 7
assert run_single_route(data) == 289
# print("A:", runner(data)) 

# B
routes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

# Test B:
def run_routes(mapdata, routes):
    multiplied = 1
    for route in routes:
        multiplied = run_single_route(mapdata,*route ) * multiplied
    return multiplied

assert run_routes(testdata, routes) == 336

# Answer B
assert run_routes(data, routes) == 5522401584
