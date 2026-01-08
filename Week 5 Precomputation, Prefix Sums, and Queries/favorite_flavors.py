import collections

Q = int(input())

cows_to_flavors = {}
flavors_to_cows = {}

for _ in range(Q):
    query = input().split()

    if query[0] == "A":
        cow, flavor = query[1], query[2]
        if cow in cows_to_flavors:
            cows_to_flavors[cow].add(flavor)
        else:
            cows_to_flavors[cow] = {flavor}

        if flavor in flavors_to_cows:
            flavors_to_cows[flavor].add(cow)
        else:
            flavors_to_cows[flavor] = {cow}

    elif query[0] == "B":
        print(len(cows_to_flavors[query[1]]))

    elif query[0] == "C":
        print(len(flavors_to_cows[query[1]]))

    else:
        for cow in flavors_to_cows[query[1]]:
            cows_to_flavors[cow].remove(query[1])
        flavors_to_cows[query[1]] = set()