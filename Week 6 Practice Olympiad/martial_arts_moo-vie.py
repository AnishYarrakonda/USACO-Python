import sys

curr_s, n = map(int, input().split())
pis = list(map(int, input().split()))

pis.sort()
if pis[0] >= curr_s:
    # Too weak to fight anyone!
    print(0)
    sys.exit(0)

curr_rep = 0
left = 0
right = n-1

while True:
    # Fight as much as possible
    while ((left < n) and (curr_s > pis[left])):
        curr_s -= pis[left]
        curr_rep += 1
        left += 1
    # If only one or zero opponents left, give up
    if left >= right:
        break
    # Might as well recruit the beefiest remaining opponent
    curr_s += pis[right]
    curr_rep -= 1
    right -= 1

print(curr_rep)