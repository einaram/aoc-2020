def read_input(day=5):
    with open(f"{day}.input.txt") as infile:
        return infile.read().splitlines()

def get_seat_id(id):
    row = int(id[:7].replace('F', '0').replace('B','1'),2)
    col = int(id[7:].replace('L', '0').replace('R','1'),2)
    return row*8+col    

def parse_all_seats(seat_strs):
    return [get_seat_id(seat) for seat in seat_strs]

def get_my_seat(all_seats):
    return [seat+1 for seat in all_seats if (not seat+1 in all_seats and seat+2 in all_seats)][0]


# A:
assert max(parse_all_seats(read_input())) == 904

#B
assert get_my_seat(parse_all_seats(read_input())) == 669


# Tests
test_cases = [
    #pass,  row, col, id
    ['BFFFBBFRRR', 70, 7, 567],
    ['FFFBBBFRRR',  14,  7, 119],
    ['BBFFBBFRLL', 102, 4, 820]]

for test_case in test_cases:
    assert get_seat_id(test_case[0]) == test_case[3]
