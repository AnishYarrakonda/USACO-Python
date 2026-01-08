Q = int(input())

for _ in range(Q):
    moo_string = input()
    if len(moo_string) < 3:
        print(-1)
        continue

    options = [ "MOO" in moo_string,
                "MOM" in moo_string or "OOO" in moo_string,
                "OOM" in moo_string]

    for i, option in enumerate(options):
        if option:
            print(len(moo_string)-3+i)
            break
    else:
        print(-1)