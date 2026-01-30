def num_compress(st):
    new_st = ''
    i = 0
    curr = None
    repeats = 0
    for i in range(len(st)):
        if st[i] == curr:
            repeats += 1
        else:
            if repeats > 0:
                new_st += str(repeats+1)
            curr = st[i]
            new_st += curr
            repeats = 0
    if repeats > 0:
        new_st += str(repeats+1)
    return new_st

def forward(st):
    st = 'b' + st + 'e'
    rotations = [st]
    for _ in range(len(st)-1):
        st = st[-1] + st[0:-1]
        rotations.append(st)
    rotations.sort()
    st = ''.join([x[-1] for x in rotations])
    return num_compress(st)

def reverse(st):
    l = len(st)
    new_st = ""
    i = 0
    while i < l:
        new_st += st[i]
        j = i + 1
        while j < l and st[j] in "0123456789":
            j += 1
        if j - i > 1:
            new_st += st[i] * (int(st[i+1:j]) - 1)
        i = j
    l = len(new_st)
    x = ["" for _ in range(l)]
    for _ in range(l):
        for i in range(l):
            x[i] = new_st[i] + x[i]
        x.sort()
    for xx in x:
        if xx[-1] == 'e':
            return xx[1:-1]

_, q = map(int, input().split())
s = input()
if q == 1:
    print(num_compress(s))
elif q == 2:
    print(forward(s))
else:
    print(reverse(s))