
arr = 939
routes_t = "7,13,x,x,59,x,31,19"


# arr=1000303
routes="41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"

def part1(routes_str):
    routes = [int(x) for x in routes_str.split(',') if x.isdigit()]

    res = [arr%x for x in routes]

    closest = [arr-re+routes[r] for r, re in enumerate(res)]

    closest_s = [x for x in sorted(closest) if x > arr][0]

    closest_r = routes[closest.index(closest_s)]

    wait = closest_s - arr

    print(wait * closest_r)



def part2(route_str):
    routes = route_str.split(',')

    routes = {int(route): r for r, route in enumerate(routes) if route.isdigit()}

    max_route = max(routes)
    t = 0
    while True:
        t+= max_route

        # [(t-routes[max_route]+routes[x]) %x == 0 for x in routes]
        #Should be faster to break after first failed
        for route in routes:
            if (t-routes[max_route]+routes[route]) % route != 0:
                break
        else:
            print("found")
            break #breaks while?
        # for r,route 
    print(t-routes[max_route])
    return t-routes[max_route]

        # if (t-4)%7 == 0:
    #     a
# assert part2(routes_t) == 1068781

# assert part2('67,7,59,61') == 754018
# assert part2('67,x,7,59,61')==   779210
# assert part2('67,7,x,59,61')==   1261476
assert part2('1789,37,47,1889')==  1202161486
# part2(routes) # 1202161486 er feil
