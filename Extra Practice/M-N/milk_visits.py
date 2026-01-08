N, M = map(int, input().split())
milk_breeds = " " + input()
adj = [[] for _ in range(N + 1)]


for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def find_path(node, end, seen=None):
    if seen is None:
        seen = set()

    seen.add(node)

    if node == end:
        return [node]

    for next_node in adj[node]:
        if next_node not in seen:
            path = find_path(next_node, end, seen)
            if path is not None:
                return [node] + path

    return None

for _ in range(M):
    u, v, breed = input().split()
    u, v = int(u), int(v)

    visited = find_path(u, v)

    for farm in visited:
        if milk_breeds[farm] == breed:
            print(1, end="")
            break
    else:
        print(0, end="")