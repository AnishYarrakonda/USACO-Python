T = int(input())

multiply = {
        ('1','1'): '1',   ('1','-1'): '-1', ('1','i'): 'i',   ('1','-i'): '-i',
        ('1','j'): 'j',   ('1','-j'): '-j',  ('1','k'): 'k',   ('1','-k'): '-k',

        ('-1','1'): '-1', ('-1','-1'): '1',  ('-1','i'): '-i', ('-1','-i'): 'i',
        ('-1','j'): '-j', ('-1','-j'): 'j',  ('-1','k'): '-k', ('-1','-k'): 'k',

        ('i','1'): 'i',   ('i','-1'): '-i',  ('i','i'): '-1', ('i','-i'): '1',
        ('i','j'): 'k',   ('i','-j'): '-k',  ('i','k'): '-j', ('i','-k'): 'j',

        ('-i','1'): '-i', ('-i','-1'): 'i',  ('-i','i'): '1',  ('-i','-i'): '-1',
        ('-i','j'): '-k', ('-i','-j'): 'k',  ('-i','k'): 'j',  ('-i','-k'): '-j',

        ('j','1'): 'j',   ('j','-1'): '-j',  ('j','i'): '-k', ('j','-i'): 'k',
        ('j','j'): '-1',  ('j','-j'): '1',   ('j','k'): 'i',  ('j','-k'): '-i',

        ('-j','1'): '-j', ('-j','-1'): 'j',  ('-j','i'): 'k',  ('-j','-i'): '-k',
        ('-j','j'): '1',  ('-j','-j'): '-1', ('-j','k'): '-i', ('-j','-k'): 'i',

        ('k','1'): 'k',   ('k','-1'): '-k',  ('k','i'): 'j',  ('k','-i'): '-j',
        ('k','j'): '-i',  ('k','-j'): 'i',   ('k','k'): '-1', ('k','-k'): '1',

        ('-k','1'): '-k', ('-k','-1'): 'k',  ('-k','i'): '-j', ('-k','-i'): 'j',
        ('-k','j'): 'i',  ('-k','-j'): '-i', ('-k','k'): '1',  ('-k','-k'): '-1',
    }

for _ in range(T):
    s = input()
    dijkstra = s[1:-4]

    total = "1"
    for c in dijkstra:
        total = multiply[(total, c)]

    if total != "-1":
        print("IMPOSSIBLE")
        continue

    running = "1"
    pos_i = -1
    for idx, c in enumerate(dijkstra):
        running = multiply[(running, c)]
        if running == "i":
            pos_i = idx
            break

    if pos_i == -1:
        print("IMPOSSIBLE")
        continue

    running = "1"
    pos_j = -1
    for idx in range(pos_i + 1, len(dijkstra)):
        running = multiply[(running, dijkstra[idx])]
        if running == "j":
            pos_j = idx
            break

    if pos_j == -1 or pos_j == len(dijkstra) - 1:
        print("IMPOSSIBLE")
        continue

    print("POSSIBLE")
