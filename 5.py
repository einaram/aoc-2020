# %%
import numpy as np

def read_input(day=5):
    with open(f"{day}.input.txt") as infile:
        return infile.read().splitlines()

def parse_seat(id_str):
    rows = list(range(0,128))
    columns = list(range(0, 8))

    for char in id_str:
        center_row = int(len(rows)/2)
        center_col = int(len(columns)/2)
        if char == 'B':
            rows = rows[center_row:]
        elif char == 'F':
            rows = rows[:center_row]
        elif char == 'L':
            columns = columns[:center_col]
        elif char == 'R':
            columns = columns[center_col:]
    return rows[0], columns[0]


def get_seat_location(seat_str):
    row, col = parse_seat(seat_str)
    return (row, col)

def get_seat_id(row,col):
    return row*8+col

# Tests
test_cases = [
    #pass,  row, col, id
    ['BFFFBBFRRR',70, 7,567],
    ['FFFBBBFRRR',  14,  7, 119],
    ['BBFFBBFRLL', 102, 4, 820]]

for test_case in test_cases:
    assert get_seat_id(*get_seat_location(test_case[0])) == test_case[3]


def parse_all_seats(seat_strs):
    return max([get_seat_id(*get_seat_location(seat)) for seat in seat_strs])


# A:
assert parse_all_seats(read_input()) == 904

# B

def create_seatmap(seat_strs):
    seatmap = np.zeros([128, 8], dtype=bool)
    for seat in seat_strs:
        row, col = parse_seat(seat)
        seatmap[row,col] = True    
    return seatmap

def find_seat(seatmap):
    rows= seatmap.sum(axis=1)

    my_row = [r for r, row in enumerate(rows) if rows[r-1] == 8 and rows[r+1] == 8 and row < 8][0]
    my_col = np.where(seatmap[my_row] == False)[0][0]
    return (my_row, my_col)

seatmap = create_seatmap((read_input()))
coord = find_seat(seatmap)
assert (get_seat_id(*coord) == 669

# %%
