def floor_average(lst: list) -> int:
    return sum(lst) // len(lst)

def simulate(n: int, ints: list) -> None:
    for i in range(n):
        ints.append(floor_average(ints))
        ints.remove(min(ints))
        print(ints)

simulate(10, [4, 5, 2])