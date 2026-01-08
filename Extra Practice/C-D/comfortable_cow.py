N = int(input().strip())

def get_adjacent_cells(cow):
    return [(cow[0] - 1, cow[1]), (cow[0] + 1, cow[1]),
            (cow[0], cow[1] - 1), (cow[0], cow[1] + 1)]

def is_comfortable(cow: tuple):
    adjacent_cells = get_adjacent_cells(cow)
    adjacent_cows = 0
    for cell in adjacent_cells:
        if cell in cow_locations:
            adjacent_cows += 1
    return int(adjacent_cows == 3)

def update_comfort(cow):
    global comfortable_count
    if cow not in cow_locations:
        return
    prev_status = cow_locations[cow]
    new_status = is_comfortable(cow)
    cow_locations[cow] = new_status
    comfortable_count += new_status - prev_status

cow_locations = {}
comfortable_count = 0

for _ in range(N):
    curr_cow = tuple(map(int, input().strip().split()))
    cow_locations[curr_cow] = is_comfortable(curr_cow)
    comfortable_count += cow_locations[curr_cow]

    for neighbor in get_adjacent_cells(curr_cow):
        update_comfort(neighbor)

    print(comfortable_count)