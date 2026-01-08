T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    if len(A) == 1:
        print(0)

    total = sum(A)
    if total == 0:
        print(0)

    factors = set()
    for i in range(1, int(total**0.5)+1):
        if total % i == 0:
            factors.add(i)
            factors.add(total // i)

    factors = sorted(list(factors))

    for factor in factors:
        groups = []
        running, running_length = 0, 0

        for num in A:
            running += num
            running_length += 1

            if running == factor:
                groups.append(running_length)
                running, running_length = 0, 0
            elif running > factor:
                break

        if sum(groups) == N:
            print(sum(map(lambda x: x-1, groups)))
            break